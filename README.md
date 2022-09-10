# Django's Custom Users🙋🏾‍♂️🙋🙋🏼‍♀️👨🏽‍🦳

There are two ways to extend users in Django: the "profile" method and a custom user. We've already used the profile method for our first project, so now we'll cover the custom user.

This project is simply about implementing a custom user from the ground up so that you can use it in the next assignment.

#### **Your Task**

Extend your custom user field so that it has the following _nullable_ field:

* Displayname (Charfield)

Implement your own 

* Signup page
* Login page (do NOT use Django's built-in login view)
* Homepage that is only accessible when logged in

The homepage should show:

*   the username of the person who is logged in
*   the displayname of the person who is logged in
*   the output the value of `settings.AUTH_USER_MODEL`

*NOTE: DO NOT name any part of your app*
'user'
_it will have conflict with the built-in user model and give you all sorts of errors that are really difficult to debug if you don't know what you're looking for._ 
Use 'custom_user', 'myuser', 'dudewheresmyuser'... _literally anything but 'user' will work._


#### Extend your custom user field so that it has the following _nullable_ fields:

*   Homepage (URLField)
*   Age (IntegerField)
-----------
#### Make the custom fields appear on the admin panel and available for editing.

#### Make the superuser command ask for their age.


