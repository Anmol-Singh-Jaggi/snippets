Problem - [Link on SPOJ](http://www.spoj.com/problems/MAIN12C/).  

**Problem statement:**  

```
Everyone loves Swampy. Swampy the Alligator lives under the city and yearns for a more human like existence.
One day Swampy thought to learn the intricacies of the internet. He went to a book store in SwampVille immediately and bought a book on "Basic Internet".
After reading the book Swampy decided to try on some exercises.
The exercise demanded Swampy to report all valid email-id's in a given free-form text string.
Check output section for exact specification.
Swampy lacks the intelligence of humans and therefore needs you to help him in this job.
The chapter defined email-id's as a string consisting of two parts.
From left to right, these are username and site-address.
The username is non-empty string of minimum length 5 build from characters {a-z A-Z 0-9. _} (excluding the brackets).
The username cannot start from '.' or '_'.
The site-address is build of a prefix which is non-empty string build from characters {a-z A-Z 0-9} (excluding the brackets) followed by one of the following suffixes {".com", ".org", "edu", ".co.in"}.
There is no space character in the email-id. The entire email-id is "username@site-address".

      Input

First line of the input contains an integer T, the number of test cases.
Then T test cases follow. Each test case consists of String S on a single line.
S is made up of characters {a-z A-Z 0-9 ~!@#$%^&*()<>?,.} (excluding the brackets) and space character too.

      Output

For each test case, print Case #X: K, where X is the test case number starting from 1, K is the number of email-id's found in S, and then K lines with email-id's found in S.

      Example

*Input:*
2
svm11@gmail.com
svm11@gmail.com svm12@gmail.co.in

*Output:*
Case #1: 1
svm11@gmail.com
Case #2: 2
svm11@gmail.com
svm12@gmail.co.in

Constraints: T <= 100 |S| <= 10000
```
