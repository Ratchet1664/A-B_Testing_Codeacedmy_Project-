import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#examines first few rows
print(ad_clicks.head())

#groups utm_source via rows and shows the total clicks
ad_platform = ad_clicks.groupby(["utm_source"]).user_id.count().reset_index()

#changing user_id to a more accurate title
ad_platform.rename(
  columns={
    'user_id':"Total views"
  },
  inplace=True
)
#print(ad_platform_views)

#creating a new column called is_click
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

#grouping the data
ad_clicks_group = ad_clicks\
  .groupby(['utm_source','is_click'])\
  .user_id.count().reset_index()

#pivoting the information
ad_clicks_pivot = ad_clicks_group.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()

ad_clicks_pivot["percent_clicked"] = ad_clicks_pivot.apply(
  lambda row: row[True] / (row[False] + row[True]),axis=1)
print(ad_clicks_pivot)

#grouping information to view with greater ease
add_comparison = ad_clicks.groupby(['experimental_group']).user_id.count().reset_index()
#print(add_comparison)

percentage = ad_clicks.groupby(["experimental_group","is_click"]).user_id.count().reset_index()

percentage_pivot = percentage.pivot(
  columns='experimental_group',
  values='user_id',
  index='is_click'
).reset_index()

print(percentage_pivot)


a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
print(a_clicks)

b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']
print(a_clicks)

a_clicks_pivot = a_clicks\
  .groupby(['is_click','day'])\
  .user_id.count()\
  .reset_index()\
  .pivot(
    index='day',
    columns='is_click',
    values='user_id')\
  .reset_index()

a_clicks_pivot['percentage'] = a_clicks_pivot[True] / \
(a_clicks_pivot[True] + a_clicks_pivot[False])

b_clicks_pivot = b_clicks\
  .groupby(['is_click','day'])\
  .user_id.count()\
  .reset_index()\
  .pivot(
    index='day',
    columns='is_click',
    values='user_id')\
  .reset_index()

b_clicks_pivot['percentage'] = b_clicks_pivot[True] / \
(b_clicks_pivot[True] + b_clicks_pivot[False])

print(a_clicks_pivot)

