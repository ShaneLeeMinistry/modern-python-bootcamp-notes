from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>First HTML Page</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text.</p>
	</div>
	<ol>
		<li class="special super-special">This list item is special.</li>
		<li class="special">This list item is also special.</li>
		<li>This list item is not special.</li>
	</ol>
	<div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_="super-special").parent.parent

data = soup.find(id="first").find_next_sibling()
data2 = data.find_previous_sibling()

print(data)
