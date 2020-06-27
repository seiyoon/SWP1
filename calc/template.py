html = b"""
<html>
    <body>
	<form method="get" action="">
	    <p>
		SUM: <input type="text" name="sum" value="%(sum)s">
	    </p>
	    <p>
		PRODUCT: <input type="text" name="product" value="%(product)s">
	    </p>
	    <p>
		sum = <input type="number" name="a">
		    + <input type="number" name="b">
	    </p>
	    <p>
		product = <input type="number" name="a">
		        * <input type="number" name="b">
	    </p>
	    <p>
		<input type="submit" value="Submit">
	    </p>
	</form>
	<p>
	    SUM: %(sum)s</br>
	    PRODUCT: %(product)s</br>
	</p>
    </body>
</html>
"""
