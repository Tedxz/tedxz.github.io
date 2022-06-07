---
layout: about
title: about
permalink: /
subtitle:

profile:
  align: right
  image: photo-main.jpg
  address: >
    <p>Photographed at XJTU in 2016</p>

news: false  # includes a list of news items
selected_papers: true # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page

bio: |
  解铮, Ph.D. Candidate  
  LAMDA Group, Nanjing University  
  Advisor: Prof. Ming Li

  I am a Ph.D. candidate of [Department of Computer Science and Technology](http://cs.nju.edu.cn/) in [Nanjing University](http://www.nju.edu.cn/), and a member of [LAMDA Group](http://www.lamda.nju.edu.cn/), led by [Prof. Zhi-Hua Zhou](http://cs.nju.edu.cn/zhouzh/). Before that, I received my B.Eng. degree in Computer Science and Technology in June 2016 from [Xi'an Jiaotong University](http://www.xjtu.edu.cn/).

  __Research Interests.__ I am interested in topics of machine learning, especially learning from imbalanced and incomplete supervision. Related topics include AUC optimization, learn to rank, positive-unlabeled learning, self-training, and semi-supervised learning on graphs.
---

<!-- https://v3.bootcss.com/css/#grid-intro -->


## Academic Services

### Journal Reviewer

- Pattern Recognition Letter  
- ACTA AUTOMATICA SINICA


### Conference PC Member
- CCML 2019, AAAI 2019  
- IJCAI 2020, ECAI 2020
- IJCAI 2021
- IJCAI 2022, ICML 2022, NeurIPS 2022


<div class="teaching-assistant">
  <h2>Teaching Assistant</h2>

  <br>
  <div class="table-responsive">
    <table class="table table-sm table-borderless">
      {% for ta in site.data.teaching-assistant %}
      <tr>
        <td>
          <span class="ta-title"> {{ ta.title }}  </span>
          {{ ta.notes | markdownify }}
        </td>
        <td align="right">
          <span class="ta-time"> For&nbsp;{{ ta.students | replace: " ", "&nbsp;" }} <br> {{ ta.semester | replace: " ", "&nbsp;" }}  </span>
        </td>
      </tr>
    {%- endfor %} 
    </table>
  </div>
</div>

<div class="honors">
  <h2>Awards & Honors</h2>

  <br>
  <div class="table-responsive">
    <table class="table table-sm table-borderless">
      {% for honor in site.data.honors %}
      <tr>
        <td>
          <!-- {{ item.content | remove: '<p>' | remove: '</p>' | emojify }} -->
          <!-- <th scope="row">{{ honor.title }}</th> -->
          <span class="honor-title"> {{ honor.title }}  </span>
        </td>
        <td align="right">
          <span class="honor-time"> {{ honor.location | replace: " ", "&nbsp;" }} <br> {{ honor.time | replace: " ", "&nbsp;" }}  </span>
        </td>
      </tr>
    {%- endfor %} 
    </table>
  </div>
</div>


## Correspondence

### Laboratory
Room 912, Computer Science Building, Xianlin Campus of Nanjing University

### Mail Address
Zheng Xie  
National Key Laboratory for Novel Software Technology,  
Nanjing University, Xianlin Campus Mailbox 603,  
163 Xianlin Avenue, Qixia District,  
Nanjing 210023, China

<!-- Link to your social media connections, too. This theme is set up to use [Font Awesome icons](http://fortawesome.github.io/Font-Awesome/) and [Academicons](https://jpswalsh.github.io/academicons/), like the ones below. Add your Facebook, Twitter, LinkedIn, Google Scholar, or just disable all of them. -->
