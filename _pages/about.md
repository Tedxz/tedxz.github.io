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
  解铮, Ph.D. &nbsp; [✉️](mailto:xiez@lamda.nju.edu.cn)  

  Currently, I am with Huawei Technologies Co., Ltd.

  I obtained my Ph.D. degree from [LAMDA Group](http://www.lamda.nju.edu.cn/) at [Nanjing University](http://www.nju.edu.cn/) in September 2023, supervised by [Prof. Ming Li](https://www.lamda.nju.edu.cn/lim/). 
  Before that, I received my B.Eng. degree in Computer Science and Technology in June 2016 from [Xi'an Jiaotong University](http://www.xjtu.edu.cn/). 

  __Research Interests.__ I am interested in topics of machine learning, especially the following aspects: 
  - __AUC Optimization__: building models for maximizing AUC from clean or potentially noisy, imbalanced, not fully supervised data. 
  - __Weakly Supervised Learning__: dealing with inaccurate, incomplete, inexact supervisions, including positive-unlabeled learning, semi-supervised learning, noisy label learning, etc. 
  - __Learning under Distribution Change__: building models for tasks whose test data distribution is different from the training data distribution, including data selection bias, covariate shift, domain adaptation, etc.
---
---

<!-- https://v3.bootcss.com/css/#grid-intro -->

<div class="working-experiences">
  <h2>Working Experience</h2>

  <br>
  {% for item in site.data.working-experience %}
  <div class="row">
    <div class="col-sm-2">
      <div class="teaser">
        {%- if item.image -%}
        {% include figure.html path=item.image class="img-fluid rounded" zoomable=false %}
        {%- endif -%}
      </div>
    </div>
    <div class="col-sm-10">
      <div class="we-title" style="line-height: 1rem;"> {{ item.title }}  </div>
      <div class="we-time-sm"> {{ item.time | replace: " ", "&nbsp;" }}  </div>
      <div class="we-time"> {{ item.time | replace: " ", "&nbsp;" }}  </div>
      {{ item.notes | markdownify }}
    </div>
  </div>
{%- endfor %} 
</div>

## Academic Services

### Journal Reviewer

- ACM Transactions on Intelligent Systems and Technology
- Pattern Recognition Letter  
- ACTA AUTOMATICA SINICA
- Knowledge-Based Systems

### Conference PC Member
- CCML 2019, AAAI 2019  
- IJCAI 2020, ECAI 2020
- IJCAI 2021
- IJCAI 2022, ICML 2022, NeurIPS 2022
- AAAI 2023, IJCAI 2023, ICML2023, NeurIPS 2023, ICLR 2023, PAKDD 2023, ECAI 2023
- AAAI 2024, IJCAI 2024, ICML 2024, NeurIPS 2024, ICLR 2024, PAKDD 2024, ECMLPKDD 2024


<div class="teaching-assistant">
  <h2>Teaching Assistant</h2>

  <br>
  {% for ta in site.data.teaching-assistant %}
  <div class="row mb-3">
    <div class="col-sm-12">
      <div class="ta-time-sm"> For&nbsp;{{ ta.students | replace: " ", "&nbsp;" }}; {{ ta.semester | replace: " ", "&nbsp;" }}.  </div>
      <div class="ta-title" style="line-height: 1rem;"> {{ ta.title }}  </div>
      <div class="ta-time"> For&nbsp;{{ ta.students | replace: " ", "&nbsp;" }} <br> {{ ta.semester | replace: " ", "&nbsp;" }}  </div>
      {{ ta.notes | markdownify }}
    </div>
  </div>
  {%- endfor %} 
</div>



<div class="honors">
  <h2>Awards & Honors</h2>

  <br>
  {% for honor in site.data.honors %}
  <div class="row">
    <div class="col-sm-12 mb-2">
      <span class="honor-title"> {{ honor.title }}  </span>
      <span class="honor-time-sm"> {{ honor.location | replace: " ", "&nbsp;" }}; {{ honor.time | replace: " ", "&nbsp;" }}.  </span>
      <span class="honor-time"> {{ honor.location | replace: " ", "&nbsp;" }} <br> {{ honor.time | replace: " ", "&nbsp;" }}  </span>
    </div>
  </div>
  {%- endfor %} 
</div>

<br><br><br>

<!--
## Correspondence

### Laboratory
Room 912, Computer Science Building, Xianlin Campus of Nanjing University

### Mail Address
Zheng Xie  
National Key Laboratory for Novel Software Technology,  
Nanjing University, Xianlin Campus Mailbox 603,  
163 Xianlin Avenue, Qixia District,  
Nanjing 210023, China
-->

{%- include statistics.html %}

<!-- Link to your social media connections, too. This theme is set up to use [Font Awesome icons](http://fortawesome.github.io/Font-Awesome/) and [Academicons](https://jpswalsh.github.io/academicons/), like the ones below. Add your Facebook, Twitter, LinkedIn, Google Scholar, or just disable all of them. -->
