#!Python
print("Content-Type: text/html")
print()

print('''<!doctype HTML>
<html>
<Head>
  <title>WEB1-HTML</title>
  <meta charset="euc-kr">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <Li><a href="index.py?id=CSS">CSS</a></li>
    <LI><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p><a href="http://www.w3.org/TR/html4/" target="_blank" title="HTML specification">Hyper Text Markup Language(HTML)</a>. Nice Library
  </p>
  <p>
   <iframe width="560" height="315" src="https://www.youtube.com/embed/ZfDq2BA1onc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </p>
  <p>
    <div id="disqus_thread"></div>
    <script>

    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
    /*
    var disqus_config = function () {
    this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://web1-agycpbzph8.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  </p>
</body>
</html>
'''.format(title="hello"))
