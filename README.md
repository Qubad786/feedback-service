
### TrueNAS UI Reviews

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About The Project](#About-The-Project)
* [Run Locally](#Run-Locally)
* [API](#API)
    + [Usage](#Usage)
    + [Add a review](#Add-a-review)
    + [Get list of reviews](#Get-list-of-reviews)
    + [Download reviews](#Download-reviews)
* [License](#license)

<!-- about -->
## About The Project

### UI reviews

TrueNAS UI reviews


#### How it Works
Users send reviews on UI pages, that are post to this project, later users can view/download user reviews.

#### Built With
* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Backend
* [Bootstrap](https://getbootstrap.com) - Frontend
* CSS for styling

#### Extensions
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - API
* [Flask-SQLalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - SQL ORM

## Run Locally
Clone using 

    $ git clone <repo-path>

Create a virtual environment for the project and activate it:

    $ virtualenv venv
    $ source venv/bin/activate

Install the required packages:

    $ pip install -r requirements.txt
    
Set the FLASK_APP environment variable:

    $ export FLASK_APP=run.py

Run the app using:

    $ flask run --host=0.0.0.0 --port=8000

Access the app in browser: http://127.0.0.1:8000/

## API
Find API docs at http://127.0.0.1:8000/api_doc


### Usage
To use the POST review API, you must provide Authorization token in the header of your request.
Example : <Authorization: Bearer {token}> token can be edited in settings.


### Add a review
Add a review

* URL: `/api/reviews/add/`
* Method: `POST`
* Header Params: Json containing the authorization token `{"Authorization": "Bearer 946bde8d85fc86c6c48344adf1ef2139"}`
* Request Body: Json containing the url and reivew `{"url": "www.trueNas.com/1", "review": "My first review"}`
* Response: review_id

Example call:
    POST: http://localhost:8000/api/reviews/add/

Example Response:
```
{
    'review_id': 1,
    'success':True
}
```

### Get list of reviews
You can get a paginated list of reviews.

* URL: `/api/reviews/`
* Method: `GET`
* Response: Returns list of reviews

Example call:

    GET  http://localhost:8000/api/reviews/?start=1&length=2

Example Response:

```
{
    "draw": 1,
    "recordsTotal": 6,
    "recordsFiltered": 2,
    "data": [
        {
            "id": "1",
            "url": "https://truenas.com/1",
            "date_created": "2022-05-16 12:18:10.339572",
            "review": "Another review"
        },
        {
            "id": "2",
            "url": "https://truenas.com/1",
            "date_created": "2022-05-16 12:18:10.969949",
            "review": "Another review"
        }
    ]
}
```

### Download reviews
You can download all reviews in a csv file (from UI or API)

* URL: `/api/reviews/export/`
* Method: `GET`
* Response: Returns list of reviews

Example call:

    GET  http://localhost:8000/api/reviews/export/

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.