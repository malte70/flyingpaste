<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		
		<title>{{!title}} :: {{!service_name}}</title>
		
		<meta name="generator" content="Flying Paste">
		<link rel="stylesheet" type="text/css" href="/style.css">
		<link rel="icon" type="image/png" sizes="96x96" href="/favicon.png">
	</head>
	<body>
		<header>
			<h1><a href="/">{{!service_name}}</a></h1>
			<h2>{{!title}}</h2>
			<p>
				This is a nopaste service, powered by
				<a href="https://github.com/malte70/flyingpaste">Flying Paste</a>.
			</p>
		</header>
		
		<main>
			<p>
				Author: {{!author_name}}<br>
				Language/File type: {{!language}}
			</p>
			<h3>Description</h3>
			<p>
				{{!description}}
			</p>
			<h3>Code</h3>
			<p>
				<code>
{{!code}}
				</code>
			</p>
		</main>
		
		<footer>
			<p>
				© 2020 <a href="https://malte70.de" rel="me nofollow">malte70</a>
			</p>
		</footer>
	</body>
</html>
