# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

BIZPATH='/Users/bencassedy/projects/yelp/yelp_phoenix_academic_dataset/yelp_academic_dataset_business.json'
USERPATH='/Users/bencassedy/projects/yelp/yelp_phoenix_academic_dataset/yelp_academic_dataset_user.json'
REVPATH='/Users/bencassedy/projects/yelp/yelp_phoenix_academic_dataset/yelp_academic_dataset_review.json'
CHECKINPATH='/Users/bencassedy/projects/yelp/yelp_phoenix_academic_dataset/yelp_academic_dataset_checkin.json'

# <codecell>

import json

# <codecell>

bizrecords = [json.loads(line) for line in open(BIZPATH)]
userrecords = [json.loads(line) for line in open(USERPATH)]
revrecords = [json.loads(line) for line in open(REVPATH)]
checkinrecords = [json.loads(line) for line in open(CHECKINPATH)]

# <codecell>

bizrecords[0]

# <codecell>

userrecords[0]

# <codecell>

revrecords[0]

# <codecell>

checkinrecords[0]

# <codecell>

from pandas import DataFrame, Series

# <codecell>

import pandas as pd; import numpy as np

# <codecell>

bizframe = DataFrame(bizrecords)
userframe = DataFrame(userrecords)
revframe = DataFrame(revrecords)
checkinframe = DataFrame(checkinrecords)

# <codecell>

bizframe_sub = DataFrame(bizrecords, columns=['business_id', 'name', 'categories', 'review_count', 'stars'])

# <codecell>

bizframe_sub.head(n=10)

# <codecell>

bsort = bizframe_sub.sort_index(by='review_count', ascending=False)

# <codecell>

bsort[:10]

# <codecell>

bizframe_sub.corr()

# <codecell>

top_biz = bizframe_sub.ix[bizframe_sub.stars == 5.0]

# <codecell>

tb = top_biz.sort_index(by='review_count', ascending=False)

# <codecell>

tb[:10]

# <codecell>

revframe

# <codecell>

rev_star_counts = revframe['stars'].value_counts()

# <codecell>

rev_star_counts[:10]

# <codecell>

user_avg_star_counts = userframe['average_stars'].value_counts()

# <codecell>

user_avg_star_counts[:10]

# <codecell>

biz_star_counts = bizframe['stars'].value_counts()

# <codecell>

biz_star_counts

# <codecell>

bizframe['stars'].describe()

# <codecell>

userframe['review_count'].describe()

# <codecell>

userframe['review_count'].skew()

# <codecell>

revframe['stars'].describe()

# <codecell>

revframe['stars'].median()

# <codecell>

rev_user_frame = pd.merge(revframe, userframe, on='user_id')

# <codecell>

rev_user_frame

# <codecell>

rev_user_sample = rev_user_frame.take(np.random.permutation(len(rev_user_frame))[:50])

# <codecell>

rev_user_sample.describe()

# <codecell>

rev_user_sample.stack()

# <codecell>

rev_user_sample.unstack()

# <codecell>

rev_user_sample.corr()

# <codecell>

group = revframe.groupby('user_id').size()

# <codecell>

group.order(ascending=False)

# <codecell>


