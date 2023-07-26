Usage
=====

``-v`` Prints the version

``url`` URL to send request to. Mandatory

``-t`` Type of request. Choose from: ``GET``, ``POST``, ``PUT``, ``PATCH``, ``DELETE``, ``OPTIONS``, ``HEAD``, ``TRACE``, ``CONNECT``

``-o``/``--output`` Outputs the recieved data to the terminal

``-p``/``--params`` URL Parameters to provide. Example ``affinity https://api.github.com/ -p foo=bar bar=foo`` 
would result in a URL of ``https://api.github.com/?foo=bar&bar=foo``. You also can provide a file by doing ``affinity https://api.github.com/ -p *params.json``

``--header`` Header data to provide. Example ``affinity https://api.github.com/ --header Content-Type=application/json`` 
would result in a URL of ``https://api.github.com/?foo=bar&bar=foo``. You also can provide a file by doing ``affinity https://api.github.com/ --header *header.json``

``--f``/``--form`` Form data to provide. Example ``affinity https://api.github.com/ --form Content-Type=application/json`` 
would result in a URL of ``https://api.github.com/?foo=bar&bar=foo``. You also can provide a file by doing ``affinity https://api.github.com/ --form *form.json``

``-e`` Change the encoding of the response. Defaults to ``UTF-8``

``--files`` List of files to send with request. Example ``affinity https://api.github.com/ --files foo.txt bar.txt``. Note that file data will be under JSON field ``files``
