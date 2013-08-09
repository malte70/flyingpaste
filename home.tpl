<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>{{!title}}</title>
		<meta name="generator" content="Flying Paste">
	</head>
	<body>
		<h1>{{!title}}</h1>
		<p>This is a nopaste service, powered by Flying Paste.</p>
		<p>
			<form action="/add" method="POST">
				<input type="text" name="title" placeholder="The Title of your paste."><br>
				<textarea name="description" placeholder="Description if title is not enough."></textarea><br>
				<input type="text" name="author_name" placeholder="Your name."><br>
				<input type="email" name="author_email" placeholder="Your EMail address."><br>
				<textarea name="code" placeholder="Your code."></textarea><br>
				<label for="language">Language: </label>
				<select size="1" name="language">
					<option value="text">Plain text/not listed below</option>
					<option value="bash">Bash script</option>
					<option value="bat">DOS/Windows Batch file</option>
					<option value="c">C</option>
					<option value="cpp">C++</option>
					<option value="css">CSS (Cascading Style Sheet)</option>
					<option value="diff">Diff/Patch file</option>
					<option value="html">HTML (with nested JavaScript and Css, too but not PHP)</option>
					<option value="irc">IRC log (irssi, xchat or weechat style log)</option>
					<option value="java">Java</option>
					<option value="js">JavaScript</option>
					<option value="json">JSON</option>
					<option value="make">Makefile</option>
					<option value="html+php">PHP (with nested HTML, JavaScript and CSS, too)</option>
					<option value="php">PHP (pure PHP, without nested HTML)</option>
					<option value="mysql">SQL (with MySQL extensions)</option>
					<option value="xml">XML</option>
					<option value="vim">VimL</option>
					<option value="yaml">YAML</option>
				</select><br>
				<label for="privacy">Privacy: </label>
				<select size="1" name="privacy">
					<option value="public">Public</option>
					<option value="not_listed">Not listed public</option>
				</select><br>
				<input type="submit" value="Add">
			</form>
		</p>
	</body>
</html>
