#include <bits/stdc++.h>
#define fastin std::ios::sync_with_stdio(false);std::cin.tie(nullptr)

using namespace std;

int main ()
{
	fastin;

	int t;
	cin >> t;
	cin.ignore();

	std::regex e ( "([a-zA-Z0-9][a-zA-Z0-9_.]{4,}@[a-zA-Z0-9]+\\.(com|co\\.in|org|edu))" );
	int k = 1;
	while ( t-- )
	{
		string s;
		getline ( cin, s );

		std::regex_iterator<std::string::iterator> rit ( s.begin(), s.end(), e );
		std::regex_iterator<std::string::iterator> rend;

		vector<string> answer;
		while ( rit != rend )
		{
			answer.push_back ( rit->str() );
			++rit;
		}

		cout << "Case #" << k++ << ": " << answer.size() << "\n";
		for ( size_t j = 0; j < answer.size(); j++ )
		{
			cout << answer[j] << "\n";
		}
	}
}
