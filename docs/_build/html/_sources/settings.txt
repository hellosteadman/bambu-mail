Settings
========

Newsletter settings
-------------------

``NEWSLETTER_PROVIDER``
	The fully-qualified module and class name of the provider to use for subscribing users to
	mailing lists

``NEWSLETTER_SETTINGS``
	A dictionary of settings to pass to the newsletter provider when a new subscription is required

Postmark settings
-----------------

``POSTMARK_API_KEY``
	The Postmark API key

``POSTMARK_SSL``
	Send data to Postmark's API via SSL (defaults to ``False``)

``POSTMARK_TEST_MODE``
	Rather than send the message to Postmark's API, simply print out the JSON data that would have
	been sent

