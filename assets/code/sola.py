import numpy as np
from sklearn.metrics import roc_auc_score


class SOLA:
    def __init__(self, gamma=0.5, zeta=0.01, R=1):
        self.__zeta = zeta  # initial step size
        self.__R = R
        self.__initialized = False
        self.__gamma = gamma

    def __initialize(self, n_dim):
        self.n_dim = n_dim

        self.__t = 0  # number of round

        self.__w = np.ones((n_dim, 1)) * np.sqrt(self.__R * self.__R / n_dim)
        self.__a1 = self.__R
        self.__a2 = self.__R
        self.__a3 = self.__R
        self.__b1 = self.__R
        self.__b2 = self.__R
        self.__b3 = self.__R
        self.__alpha1 = 2 * self.__R
        self.__alpha2 = 2 * self.__R
        self.__alpha3 = 2 * self.__R
        self.__np = 0
        self.__nn = 0
        self.__nu = 0

        self.__initialized = True

    def predict_score(self, x):
        x = x.reshape((-1, 1))
        if not self.__initialized:
            self.__initialize(x.shape[0])
        return np.dot(self.w.T, x)

    def predict(self, x):
        print('predict function for AUC optimization is not defined.')
        x = x.reshape((-1, 1))
        return np.sign(self.predict_score(x))

    def update(self, x, y):
        if not self.__initialized:
            self.__initialize(x.shape[0])
        x = x.reshape((-1, 1))

        n_dim = self.n_dim

        self.__t += 1
        self.__labeled_cnt += (y == +1)

        eta = self.__zeta / np.sqrt(self.__t)  # step size

        gamma = self.__gamma
        wx = np.dot(self.__w.T, x)

        # gradient
        Fpn_w, Fpu_w, Fun_w = 0, 0, 0
        if y == +1:
            self.__np += 1

            Fpn_a1 = self.__nn * 2 * (self.__a1 - wx)
            Fpu_a2 = self.__nu * 2 * (self.__a2 - wx)
            self.__a1 -= eta * gamma * Fpn_a1
            self.__a2 -= eta * (1 - gamma) * Fpu_a2
            
            Fpn_alpha1 = self.__nn * -2 * wx - 2 * self.__np * self.__nn * self.__alpha1 / (self.__np + self.__nn)
            Fpu_alpha2 = self.__nu * -2 * wx - 2 * self.__np * self.__nu * self.__alpha2 / (self.__np + self.__nu)
            self.__alpha1 += eta * gamma * Fpn_alpha1
            self.__alpha2 += eta * (1 - gamma) * Fpu_alpha2

            Fpn_w = (2 * (wx - self.__a1) * x - 2 * (1 + self.__alpha1) * x) * self.__nn
            Fpu_w = (2 * (wx - self.__a2) * x - 2 * (1 + self.__alpha2) * x) * self.__nu
        elif y == -1:
            self.__nn += 1

            Fpn_b1 = self.__np * 2 * (self.__b1 - wx)
            Fun_b3 = self.__nu * 2 * (self.__b3 - wx)
            self.__b1 -= eta * gamma * Fpn_b1
            self.__b3 -= eta * (1 - gamma) * Fun_b3

            Fpn_alpha1 = self.__np * +2 * wx - 2 * self.__np * self.__nn * self.__alpha1 / (self.__np + self.__nn)
            Fun_alpha3 = self.__nu * +2 * wx - 2 * self.__nu * self.__nn * self.__alpha3 / (self.__nu + self.__nn)
            self.__alpha1 += eta * gamma * Fpn_alpha1
            self.__alpha3 += eta * (1 - gamma) * Fun_alpha3

            Fpn_w = (2 * (wx - self.__b1) * x + 2 * (1 + self.__alpha1) * x) * self.__np
            Fun_w = (2 * (wx - self.__b3) * x + 2 * (1 + self.__alpha3) * x) * self.__nu
        elif np.isnan(y):
            self.__nu += 1

            Fpu_b2 = self.__np * 2 * (self.__b2 - wx)
            Fun_a3 = self.__nn * 2 * (self.__a3 - wx)
            self.__b2 -= eta * (1 - gamma) * Fpu_b2
            self.__a3 -= eta * (1 - gamma) * Fun_a3

            Fpu_alpha2 = self.__np * +2 * wx - 2 * self.__np * self.__nu * self.__alpha2 / (self.__np + self.__nu)
            Fun_alpha3 = self.__nn * -2 * wx - 2 * self.__nu * self.__nn * self.__alpha3 / (self.__nu + self.__nn)
            self.__alpha2 += eta * (1 - gamma) * Fpu_alpha2
            self.__alpha3 += eta * (1 - gamma) * Fun_alpha3

            Fpu_w = (2 * (wx - self.__b2) * x + 2 * (1 + self.__alpha2) * x) * self.__np
            Fun_w = (2 * (wx - self.__a3) * x - 2 * (1 + self.__alpha3) * x) * self.__nn
        else:
            assert False

        self.__w -= eta * (gamma * Fpn_w + (1 - gamma) * (Fpu_w + Fun_w))


        # projection w to the hyperball
        w_norm = np.linalg.norm(self.__w)
        if w_norm > self.__R:
            self.__w *= self.__R / w_norm
        # self.__a1 = min(self.__a1, self.__R)
        # self.__b1 = min(self.__b1, self.__R)
        # self.__alpha1 = min(max(self.__alpha1, -2 * self.__R), 2 * self.__R)
        # self.__a2 = min(self.__a2, self.__R)
        # self.__b2 = min(self.__b2, self.__R)
        # self.__alpha2 = min(max(self.__alpha2, -2 * self.__R), 2 * self.__R)
        # self.__a3 = min(self.__a3, self.__R)
        # self.__b3 = min(self.__b3, self.__R)
        # self.__alpha3 = min(max(self.__alpha3, -2 * self.__R), 2 * self.__R)


    @property
    def w(self):
        return np.copy(self.__w)

    def __str__(self):
        return ('SOLA (gamma=%.2f, zeta=%.2f, R=%.2f)' %
                (self.__gamma, self.__zeta, self.__R))

class Samult:
    def __init__(self, lambda_=1, gamma=0.5):
        self.__lambda = lambda_
        self.__gamma = gamma

    def train(self, xp, xn, xu):
        from numpy.linalg import pinv as pinv
        from numpy.linalg import inv as inv

        n_feature = xp.shape[1]
        n_p = xp.shape[0]
        n_n = xn.shape[0]
        n_u = xu.shape[0]
        # print(n_p, n_n, n_u)
        assert n_p * n_n * n_u > 0

        xptxp = np.dot(xp.T, xp) / n_p
        xntxn = np.dot(xn.T, xn) / n_n
        xutxu = np.dot(xu.T, xu) / n_u

        meanxp = np.mean(xp.T, axis=1, keepdims=True)
        meanxn = np.mean(xn.T, axis=1, keepdims=True)
        meanxu = np.mean(xu.T, axis=1, keepdims=True)

        h_pu = (meanxp - meanxu)
        h_pn = (meanxp - meanxn)
        h_un = (meanxu - meanxn)

        H_pu = xptxp - np.dot(meanxu, meanxp.T) - np.dot(meanxp, meanxu.T) + xutxu
        H_pn = xptxp - np.dot(meanxn, meanxp.T) - np.dot(meanxp, meanxn.T) + xntxn
        H_un = xutxu - np.dot(meanxn, meanxu.T) - np.dot(meanxu, meanxn.T) + xntxn

        w = np.dot(pinv((1-self.__gamma) * (H_pu + H_un) + self.__gamma * H_pn + self.__lambda * np.eye(n_feature)), ((1-self.__gamma)*(h_pu + h_un) + self.__gamma * h_pn))  # My PNU
        self.__w = w


    def predict(self, x):
        x = x.reshape((-1, 1))
        return np.sign(self.predict_score(x))

    @property
    def w(self):
        return np.copy(self.__w)

    def __str__(self):
        return ('Samult (gamma=%.2f, lambda=%.2f)' %
                (self.__gamma, self.__lambda))

def main():
    # generate a toy dataset for testing
    # other dataset needs normalize before using, or the algorithm may not converge
    X = np.random.normal(0, 1, (5000, 2))
    X_test = np.random.normal(0, 1, (5000, 2))
    w = np.random.normal(0, 1, (2, 1))

    ground_truth = np.sign(X @ w)
    Y = ground_truth.copy()
    Y[np.random.choice(5000, 4000)] = np.nan  # remove 4000 labels
    Y_test = np.sign(X_test @ w)

    print('-------- SOLA --------')
    model = SOLA(zeta=0.001)
    for i in range(X.shape[0]):
        model.update(X[i, :], Y[i])
        # print('AUC', roc_auc_score(ground_truth, X @ model.w))
    
    print('AUC', roc_auc_score(ground_truth, X @ model.w))
    print('AUC on test set', roc_auc_score(Y_test, X_test @ model.w))

    print('-------- Samult --------')
    model = Samult()
    Y = Y.reshape(-1)
    xp = X[Y == 1, :]
    xn = X[Y == -1, :]
    xu = X[np.isnan(Y), :]
    model.train(xp, xn, xu)
    print('AUC', roc_auc_score(ground_truth, X @ model.w))
    print('AUC on test set', roc_auc_score(Y_test, X_test @ model.w))


if __name__ == "__main__":
    main()