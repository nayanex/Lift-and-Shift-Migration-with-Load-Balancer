import logging
import azure.functions as func
import json
from json import JSONEncoder
import os

class Review:
    def __init__(self, name, email, company, job_position, review):
        self.name = name
        self.email = email
        self.company = company
        self.job_position = job_position
        self.review = review
class ReviewEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
data = [
        Review(name='Enoch Josh',
              email='enoch@josh.com',
              company= 'Mouelet Medical Center',
              job_position='Medical Chief Officer',
              review= 'I recommend this book to all my medical students because lessons, ' +
                      'stories, advices from this artistic work applies both in engineering as well as' +
                      ' in the medical field.'),
        Review(name='Lily Michele',
              email='lily@michele.org',
              company= 'TOKO LLC',
              job_position= 'Chief Data Scientist',
              review= 'I wish I had a role mole like her to outline my goals and dreams in order'+
                      ' to avoid the common mistakes of a young and enthusiastic engineer. ' +
                      'Buy, read and offer a copy to someone younger than you!'),
        Review(name='Laidry Arian',
              email='laidry@arian.edu',
              company= 'MabInvestment',
              job_position= 'CEO',
              review= 'This a classic GPS for this generation; it outlines what to do, what not to do,'+
                      ' when to do it, how to do it, and why taking the risk is the greatest legacy you' +
                      ' can ever give yourself.')
        ]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == 'GET':

        return func.HttpResponse(json.dumps(data, cls=ReviewEncoder))
    else:
        review = Review(req.form['name'],
                        req.form['email'],
                        req.form['company'],
                        req.form['jobPosition'],
                        req.form['review'])
        data.append(review)
        return func.HttpResponse(json.dumps(data, cls=ReviewEncoder))