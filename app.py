
''' my flask application runner'''

from mobash_blog import app


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # run with the debug mode    
