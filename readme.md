# Panipuri

Panipuri is a library to cache scraped data. It's intended mainly for data analysists working in the interactive console or at the command line.

Totally not ready for mainstream usage at all right now.

## Rationale

Suppose I'm writing a data analysis script based on pulling data out of the Facebook graph API and then doing something with it. I'd probably build a function like this:

    def pull_from_facebook(url):
        return requests.get("https://api.facebook.com/method/fql.query?query=select%20total_count,like_count,comment_count,share_count,click_count,normalized_url%20from%20link_stat%20where%20url=%27"+ url + "%27&format=json")

This means that every time I run the script, I'm using up my quota of Facebook requests. Additionally, the script will be slow to run.

Panipuri is a simple (local) caching library to avoid that:

    from panipuri import simple_cache

    @simple_cache("/tmp/fb_graph_queries.db")
    def pull_from_facebook(url):
        return requests.get("https://api.facebook.com/method/fql.query?query=select%20total_count,like_count,comment_count,share_count,click_count,normalized_url%20from%20link_stat%20where%20url=%27"+ url + "%27&format=json")

## Installation

Standard installation:

    $ python setup.py install

## Usage

There are multiple cache backends to use. The default is a [DBM](https://docs.python.org/2/library/dbm.html) cache. There is also a SQLite cache, which can be used as follows:

    from panipuri.backends import *

    @simple_cache(SQLiteCache("/tmp/mydb.sqlite", "facebook_table"))
    def pull_from_facebook(url):
        return requests.get("https://api.facebook.com/method/fql.query?query=select%20total_count,like_count,comment_count,share_count,click_count,normalized_url%20from%20link_stat%20where%20url=%27"+ url + "%27&format=json")
