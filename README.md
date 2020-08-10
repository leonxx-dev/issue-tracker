[![Build Status](https://travis-ci.org/Leon2ev/issue-tracker.svg?branch=master)](https://travis-ci.org/Leon2ev/issue-tracker)
<h1><a href="https://jevgeni-issue-tracker.herokuapp.com/">
    Issue Tracker on Heroku
</a></h1>
<p>
    Any good project should have a system that can connect users with developers
    and opposite. Users can easily report about issues that they found or ask to 
    implement some features that they would like to see in your project. To 
    prioritize users needs there will be an upvoting system, that will help users
    to push on the top of the list the most common issue or feature.This system
    will help developers to understand users needs and improve it.
</p>
<p>
    Issues will be fixed for free and can be upvoted for free as well. But if 
    users missing something in your project and willing to have it in the future, 
    for amount of money of users choice they can create a feature ticket with 
    detailed description of their needs, upvotes for this tickets as well for 
    amount of money of users choice.
</p>

<h2>UX</h2>
<p>
    Issue trecker can be part of any project. It connects users with developers.
    Using issue-tracker users can tell developers about issues that they found
    and tell develepors what they want to see in future. Users can upvote each
    other tickets. So developers can see what is the most important problems 
    and try to fix it first.
</p>
<ul>
    <li>
        As user who found an issue in product. I can go to tickets page and try 
        to find if someone else had this issue using searchbar and other filters
        if I found the similar issue I can upvote it.
    </li>
    <li>
        As user who found an issue in product. And there is nothing similar on 
        the tickets page I can create a new ticket and describe in details the 
        issue. In this case I will let developers to know that there is a problem.
    </li>
    <li>
        As regular user I start to undestand that I missing something in this 
        product. And it will cool to implement that. I can go and check if 
        someone else have the same needs. If I found that my idea is on someones
        ticket, I give him an upvote.
    </li>
    <li>
        As regular user I start to undestand that I missing something in this 
        product. And it will cool to implement that. And there is nothing similar 
        on the tickets page I can create a new ticket and describe in details 
        my great idea.
    </li>
    <li>
        As user I would see if there any progress going with the issue or 
        feature tickets. And I can see it by status 'Pending', 'In Progress' or 
        'Done'. It helps me to see how active are developers.
    </li>
    <li>
        As user I found one ticket and after readind description I know hoe to
        make it a bit better way. In this case I can leave a comment under the 
        ticket.
    </li>
</ul>
<a href="https://balsamiq.cloud/s4y4k8d/pflz15h/r69ED">Wireframe</a>
<a href="https://dbdesigner.page.link/NC6SXJAb8SXv5cUW8">Database schema</a>
<h2>Features</h2>
<h3>Existing Features</h3>
<ul>
    <li>
        Tickets Page
        <ul>
            <li>Filters - that helps users find tickets that they looking for</li>
            <li>
                Each ticket have 2 colorful labels that changing color dynamically
                depence of the ticket type or status
            </il>
            <li>Add Ticket - redirect to create ticket form</li>
            <li>Read More - redirect to ticket detail page</li>
        </ul>
    </li>
    <li>
        Ticket Detail Page 
        <ul>
            <li>
                UpVote - every user can provide a vote for ticket. User can vote 
                once for Issue and there is no limit for Feature. By pressing 
                upvote feature it will redirect to prepayment page where user 
                should insert amount that he willing to pay
            </li>
            <li>
                Comment - users can write a comment under each ticket
            </li>
            <li>Edit Ticket - available only for ticket author</li>
        </ul>
    </li>
    <li>
        Ticket Form Page
        <ul>
            <li>
                Create Ticket - creates a new ticket. By creating feature 
                ticket it will redirect to prepayment page where user 
                should insert amount that he willing to pay
            </li>
            <li>
                Edit Ticket - makes change to existing ticket. If user want to 
                change ticket type from issue to feature he should pay
            </li>
        </ul>
    </li>
    <li>
        Prepayment page 
        <ul>
            <li>
                Insert Amount - users get chance to insert amount that they 
                willing to pay for upvote or feature ticket. After submiting 
                item will be added to the cart and user will redirected to 
                tickets page
            </li> 
        </ul>
    </li>
    <li>
        Cart
        <ul>
            <li>
                Item List - in cart users have list of items they want to vote for
                or create. No actions is apply before they pay. User can delete 
                items from the cart
            </li> 
            <li>
                Checkout - redirect to checkout form
            </li>
        </ul>
    </li>
    <li>
        Checkout
        <ul>
            <li>
                Checkout - user have to fill up personal information and credit
                card details. After submiting the payment if payment went well 
                users tickets and votes will appear in the system
            </li>
        </ul>
    </li>
</ul>
<h3>Features Left to Implement</h3>
<ul>
    <li>
        Password reset will send real email. Now only in terminal.
    </li>
    <li>
        User profile with recent activity(tickets created, votes, comments).     
    </li>
    <li>
        Dasboard.     
    </li>
</ul>
<h2>Technologies Used</h2>
<ul>
    <li>
        <a href="https://getbootstrap.com/docs/3.3/getting-started/">Bootstrap</a>
        <ul>
            <li>For template and to make website mobile responsive.</li>
        </ul>
    </li>
    <li>
        <a href="https://docs.djangoproject.com/en/2.2/">Django</a>
        <ul>
            <li>Full stack framework.</li>
        </ul>
    </li>
    <li>
        <a href="https://www.postgresql.org/">Postgres</a>
        <ul>
            <li>SQL database base for our data.</li>
        </ul>
    </li>
    <li>
        <a href="https://pypi.org/project/python-dotenv/">Dotenv</a>
        <ul>
            <li>
                Reads the key,value pair from env.py file and adds them to 
                environment variable. It is great for managing app settings during 
                development and in production using 12-factor principles.
            </li>
        </ul>
    </li>
    <li>
        <a href="https://caolan.github.io/async/queue.js.html">JQuery</a>
        <ul>
            <li>Used for simplify DOM manipulation.</li>
        </ul>
    </li>
    <li>
        <a href="https://aws.amazon.com/s3/">Amazon S3</a>
        <ul>
            <li>Used for storing static files.</li>
        </ul>
    </li>
    <li>
        <a href="https://stripe.com/en-no">Stripe</a>
        <ul>
            <li>Used for handling payments.</li>
        </ul>
    </li>
    <li>
        <a href="https://www.psycopg.org/docs/">Psycopg</a>
        <ul>
            <li>Used for implementing the DB API 2.0 protocol.</li>
        </ul>
    </li>
    <li>
        <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">
            Boto3
        </a>
        <ul>
            <li>
                Used to create, configure, and manage AWS services, such as EC2 
                and S3. Boto provides an easy to use, object-oriented API, as well 
                as low-level access to AWS services.
            </li>
        </ul>
    </li>
    <li>
        <a href="https://gunicorn.org/">Gunicorn</a>
        <ul>
            <li>Used for deploy project on heroku.</li>
        </ul>
    </li>
</ul>
<h2>Testing</h2>
<h3>Automated tests</h3>
<p>
    There is some automated tests in the project. To run them use commant:
</p>
<ul>
    <li>
        $python manage.py test      
    </li>
</ul>
<p>
    To see the test report:
</p>
<ul>
    <li>
        $ coverage run manage.py test  
        $ coverage html   
    </li>
</ul>
<h3>Manual Tests</h3>
<p>
    All tests going from top and from left to right
</p>
<p>
    During the test on different devices and browsers no problems has been found.
</p>
<h5>Navigation</h5>
<ul>
    <li>
        Logo, links on navigation bar working well.    
    </li>
</ul>
<h5>Tickets Page</h5>
<ul>
    <li>
        Filters working well. I can filter using multi paramenters.
    </li>
    <li>
        Add Product button open a page form how it should be. Only if user 
        logged in. If not redirect to login.
    </li>
    <li>
        Read more button open a product description page how it should be.
    </li>
</ul>
<h5>Ticket Detail Page</h5>
<ul>
    <li>
        Votes working well. Vote can only if logged in. For Issue one vote per 
        person. For Feature no limit but users have to pay it will redirect to 
        prepaymentpage
    </li>
    <li>
        Comments working well. User can leave comment only if logged in.  
    </li>
    <li>
        Edit Ticket working well. Login required. Edit ticket can only author.
    </li>
    <li>
        Label colors ticket type(Issue/Feature) and ticket 
        status(Pending/In Progress/Done) changing dynamically.
    </li>
</ul>
<h5>Ticket Form Page</h5>
<ul>
    <li>
        For Create a ticket. All fields required. For Issue if form filled up 
        and submited it appears on tickets page. If it Feature it will redirect 
        to prepayment page. It will create ticket in database but it will be 
        hidden until it's paid. 
    </li>
    <li>
        For Edit a ticket. All fields required. Data appear from the right ticket.
        If user want to change ticket type from Issue to Feature and submit it 
        will redirect to prepayment page like in example above.
    </li>
</ul>
<h5>Prepayment Page</h5>
<ul>
    <li>
        Input field working well not allowed to add amount less than 100 NOK.
        If submit amount added to ticket and added in to the cart and redirect 
        to tickets page.
    </li>
</ul>
<h5>Cart</h5>
<ul>
    <li>
        User can see all items in the cart, amount per item and total amount.
    </li>
    <li>
        User can remove items from the cart.
    </li>
    <li>
        Checkout button will redirect to payment form.
    </li>
</ul>
<h5>Checkout</h5>
<ul>
    <li>
        Form cannot be submited empty.
    </li>
    <li>
        During the tests. Use test credit card details.
        <ul>
            <li>Card number: 4242 4242 4242 4242</li>
            <li>ccv: any three numbers</li>
            <li>Date: any future date</li>
        </ul>
    </li>
</ul>
<h3>Bugs</h3>
<p>
    At the moment couldn't implement pagination because conflict with 
    django-filter. Didn't found any information how to fix it.
</p>
<h2>Deployment to Heroku</h2>
<ol>
    <li>Log in to Heroku</li>
    <li>Create new app. Select App name and server region.</li>
    <li>Go to resources and find postrges in add-ons.</li>
    <li>Create travis integration.
        <ul>
            <li>Login to travis with github.</li>
            <li>
                Add .travis.yml file with language information, version, 
                requirements.txt and script.
            </li>
            <li>
                Add line of code to README.md file to see if project passing 
                tests.
            </li>
        </ul>
    </li>
    <li>Create file with dependencies. pip freeze > requirements.txt</li>
    <li>env_sample.py file with all environ variables needed to run project</li>
    <li>Create Profile. web: gunicorn issuetracker.wsgi:application</li>
    <li>Create git repository. Git init, git add.</li>
    <li>Log in to heroku. heroku login -i</li>
    <li>Connect to heroku repository. heroku git:remote -a {your-project-name}</li>
    <li>Push to heroku. git push heroku master</li>
</ol>
<h2>Run locally</h2>
<ol>
    <li>Create virtual evniroment</li>
    <li>pip install -r requiremnt.txt</li>
    <li>
        Check env_sample.py file with all environ variables needed to run project
    </li>
</ol>
<h2>Credits</h2>
<h3>Media</h3>
<a href="http://adwallpapers.xyz/146894-albion-online-4k-ultra-hd-wallpaper.html">
Background image</a>