# Detect-phishing-websites-using-ML

This project is a simple example which trains the model to predict phishing websites. Phishing websites are fake websites which try to gain the trust of users to steal private data of users.
* Best accuracy score - **97.0%** using Random forest method
* Worst accuract score - **48.5%** using One class svm method

### Requirements
* Scikit-learn (sklearn)
* Numpy

Requirements can be installed by executing `pip install -r requirements.txt`

### Data set 
The data set for training has been taken from [UCI archive](https://archive.ics.uci.edu/ml/machine-learning-databases/00327/Training%20Dataset.arff)

### Execution
* `python classifier.py` to check the accuracy of the script.
* `python classifier.py google.com` to check whether google.com is phishing website or not.

#### Parameters in dataset
Each value in the dataset contains all these elements and all are seperated by a comma.
1. having_IP_Address  { -1,1 }
2. URL_Length   { 1,0,-1 }
3. Shortining_Service { 1,-1 }
4. having_At_Symbol   { 1,-1 }
5. double_slash_redirecting { -1,1 }
6. Prefix_Suffix  { -1,1 }
7. having_Sub_Domain  { -1,0,1 }
8. SSLfinal_State  { -1,1,0 }
9. Domain_registeration_length { -1,1 }
10. Favicon { 1,-1 }
11. port { 1,-1 }
12. HTTPS_token { -1,1 }
13. Request_URL  { 1,-1 }
14. URL_of_Anchor { -1,0,1 }
15. Links_in_tags { 1,-1,0 }
16. SFH  { -1,1,0 }
17. Submitting_to_email { -1,1 }
18. Abnormal_URL { -1,1 }
19. Redirect  { 0,1 }
20. on_mouseover  { 1,-1 }
21. RightClick  { 1,-1 }
22. popUpWidnow  { 1,-1 }
23. Iframe { 1,-1 }
24. age_of_domain  { -1,1 }
25. DNSRecord   { -1,1 }
26. web_traffic  { -1,0,1 }
27. Page_Rank { -1,1 }
28. Google_Index { 1,-1 }
29. Links_pointing_to_page { 1,0,-1 }
30. Statistical_report { -1,1 }
31. Result  { -1,1 }
