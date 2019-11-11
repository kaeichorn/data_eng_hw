i.
queries were run using pgadmin container

What is the number of unique users?
```select count(distinct user_id) from "user"``` 2902

ii.
Who are the marketing ad providers?
```select distinct provider from marketing```

null <- null value from incomplete data
"Instagram"
"Facebook"
"Inst" <- bad data
"Snapchat"
"Spotify"

iii.
Which user property is changed the most frequently?
I interpreted "changed most frequently" as any input or update to the value. Example: for user_id = '3f5e74dbdcf92513db71959e97c07fe5', 
the property drinking received 5 inputs or updates. Sex also received 5. (Query ```select * from "user" where user_id = '3f5e74dbdcf92513db71959e97c07fe5'
order by property;```)

So to answer the question - Drinking was changed most frequently  

```select property, count(distinct (event_id)) from "user" group by property order by count(event_id) desc```

iv.
How many users where shown a Snapchat ad on July 3rd, 2019?
i interpreted this as unique users. Answer 236
```select count(distinct user_id) 
from marketing join "user" on marketing.phone_id ="user".phone_id
where marketing.provider='Snapchat' and date(marketing.event_ts)='2019-07-03'```

there were 749 Snapchat 'events' on that day
```select count(marketing.event_id) 
from marketing join "user" on marketing.phone_id ="user".phone_id
where marketing.provider='Snapchat' and date(marketing.event_ts)='2019-07-03'```

v.
Which ad was showed the most to users who identify as moderates?
ad_id 4 was showed the most to users who identified as moderates at that time. 

```select ad_id,count(*) from 
marketing inner join "user" on marketing.phone_id ="user".phone_id
where property='politics' and "value"='Moderate'
group by ad_id
order by count(*) desc```

vi.
What are the top 5 ads? Explain how you arrived at that conclusion.
Since we don't have conversion data (whether or not a user performed an action related to the ad), I define a top or successful ad as seen by the most eyeballs. In this dataset, it would be having the most events. I interpret that as appearing on the screen. Also an ad would be successful if it's shown a lot based on the user prefrences. So if an ad is shown that means it must align with the user property values that they entered, and a successful ad has appeal to more users in the user base. 

```select ad_id,count(event_id) from marketing group by ad_id order by COUNT(*) desc limit 5```

|ad_id | count()|
--------------
|"1"| "745"|
|"4"|	"731"|
|"2"|	"689"|
|"3"|	"673"|
|"0"|	"672"|
