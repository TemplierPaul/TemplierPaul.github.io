---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


{% include base_path %}
{% if site.author.googlescholar %}
You can find an updated list of my articles on my <a href="{{site.author.googlescholar}}">Google Scholar profile</a>.
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
