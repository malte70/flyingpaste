<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		
		<title>{{!title}}</title>
		
		<meta name="generator" content="Flying Paste">
		<link rel="stylesheet" type="text/css" href="/assets/css/style.css">
		<link rel="icon" type="image/png" sizes="96x96" href="/assets/img/favicon.png">
	</head>
	
	<body id="top">
		<header>
			<h1><a href="/">{{!title}}</a></h1>
			<p>
				This is a semi-public nopaste service, powered by
				<a href="https://github.com/malte70/flyingpaste">Flying Paste</a>.
			</p>
			<!--<p>
				Spam and otherwise suspicious content may be removed at any time without a warning.
			</p>-->
			<p>
				Although this service is publicly accessible and anyone can create pastes, it
				is primarily intended for internal use.
			</p>
			<p>
				Spam, or otherwise suspicious content can be deleted at any time without warning.
				The permanent storage of uploads is not guaranteed!
			</p>
			<p>
				Possibly illegal content, pastes without code or with a suspicious description, as
				well as pastes with links to adult content/spam sites/scam sites will be removed!
			</p>
		</header>
		
		<main>
			<section id="add">
				<p>
					<form action="/add" method="POST">
						<input type="text" name="title" placeholder="The Title of your paste." required>
						
						<textarea name="description" placeholder="Description if title is not enough."></textarea>
						
						<input type="text" name="author_name" placeholder="Your name." required>
						
						<input type="email" name="author_email" placeholder="Your EMail address." required>
						
						<textarea name="code" placeholder="Your code." required></textarea>
						
						<span class="group">
							<label for="language">Language: </label>
							<select size="1" name="language">
								<option value="text">Plain text/not listed below</option>
								<option value="apacheconf">Apache Config (.htaccess, apache.conf)</option>
								<option value="ahk">AutoHotKey</option>
								<option value="applescript">AppleScript</option>
								<option value="arduino">Arduino</option>
								<option value="aspx-vb">ASP.NET (with embedded Visual Basic.NET)</option>
								<option value="gas">Assembler (gas)</option>
								<option value="nasm">Assembler (NASM)</option>
								<option value="tasm">Assembler (TASM)</option>
								<option value="awk">Awk</option>
								<option value="bash">Bash script</option>
								<option value="shell-session">Bash session</option>
								<option value="bat">DOS/Windows Batch file</option>
								<option value="c">C</option>
								<option value="cbmbas">CBM BASIC V2</option>
								<option value="cmake">CMake</option>
								<option value="coffee">CoffeeScript</option>
								<option value="cpp">C++</option>
								<option value="css">CSS (Cascading Style Sheet)</option>
								<option value="diff">Diff/Patch file</option>
								<option value="genshi">Genshi</option>
								<option value="groff">Groff</option>
								<option value="haml">Haml</option>
								<option value="hexdump">Hexdump</option>
								<option value="html">HTML (with nested JavaScript and Css, too but not PHP)</option>
								<option value="http">HTTP</option>
								<option value="ini">INI (.ini, .inf, .cfg)</option>
								<option value="iptables">Iptables</option>
								<option value="irc">IRC log (irssi, xchat or weechat style log)</option>
								<option value="java">Java</option>
								<option value="js">JavaScript</option>
								<option value="jcl">JCL</option>
								<option value="json">JSON</option>
								<option value="kconfig">Kconfig (Linux Kernel Config)</option>
								<option value="dmesg">Kernel log (dmesg)</option>
								<option value="less">LESS CSS</option>
								<option value="lighttpd">Lighttpd config</option>
								<option value="lua">Lua</option>
								<option value="make">Makefile</option>
								<option value="mathematica">Mathematica (.nb, .cdf, .nbp, .ma)</option>
								<option value="matlab">Matlab (.m)</option>
								<option value="md">Markdown</option>
								<option value="nginx">nginx Config</option>
								<option value="pacmanconf">pacman.conf</option>
								<option value="perl">Perl</option>
								<option value="perl6">Perl 6</option>
								<option value="html+php">PHP (with nested HTML, JavaScript and CSS, too)</option>
								<option value="php">PHP (pure PHP, without nested HTML)</option>
								<option value="po">Gettext Catalog (.po, .pot)</option>
								<option value="PowerShell">PowerShell</option>
								<option value="properties">.properties</option>
								<option value="pycon">Python Console Session</option>
								<option value="pytb">Python Traceback</option>
								<option value="python2">Python 2</option>
								<option value="python3">Python 3</option>
								<option value="r">R</option>
								<option value="rust">Rust (.rs)</option>
								<option value="scss">SCSS</option>
								<option value="smarty">Smarty</option>
								<option value="sourceslist">Debian sources.list</option>
								<option value="sql">SQL</option>
								<option value="mysql">SQL (with MySQL extensions)</option>
								<option value="sqlite">SQL (SQLite3 console)</option>
								<option value="tcl">Tcl</option>
								<option value="tex">TeX</option>
								<option value="todotxt">todo.txt</option>
								<option value="typescript">TypeScript</option>
								<option value="vb.net">VisualBasic.NET</option>
								<option value="vim">VimL</option>
								<option value="xml">XML</option>
								<option value="xorg.conf">Xorg.conf</option>
								<option value="xslt">XSLT</option>
								<option value="yaml">YAML</option>
							</select>
						</span>
						
						<!--<span class="group" style="display:none">-->
						<span class="group">
							<label for="privacy">Privacy: </label>
							<select size="1" name="privacy">
								<option value="public" selected>Public</option>
								<option value="not_listed">Not publicly listed</option>
							</select>
						</span>
						
						<span class="group">
							<button type="submit">Add</button>
						</span>
					</form>
				</p>
			</section>
			
			<section id="list">
				<h3>Recently added public pastes</h3>
				<ul>
					% for paste in pastes:
					<li>
						<a href="/p/{{!paste["id"]}}.html">{{!paste["title"]}}</a> <i>(<em>{{!languages[paste["language"]]}}</em> by <em>{{!paste["author"]}}</em>)</i>
					</li>
					% end
				</ul>
			</section>
		</main>
		
		<footer>
			<p>
				© {{!year}} <a href="https://malte70.de" rel="me nofollow">malte70</a>
			</p>
		</footer>
	</body>
</html>
