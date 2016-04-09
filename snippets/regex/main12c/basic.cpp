#include <bits/stdc++.h>
#define fastin std::ios::sync_with_stdio(false);std::cin.tie(nullptr)
using namespace std;


bool IsValidUserNameChar ( const char& c )
{
	return isalnum ( c ) || c == '.' || c == '_';
}


bool IsValidSiteAddressChar ( const char& c )
{
	return isalnum ( c );
}


bool IsValidUserName ( const string& userName )
{
	return userName.size() >= 5 && userName[0] != '.' && userName[0] != '_';
}


int main()
{
	//fastin;
	const vector<string> suffixes = {".com", ".org", ".edu", ".co.in"};

	int t, k = 1;
	cin >> t;
	cin.ignore();

	while ( t-- )
	{
		string line;
		getline ( cin, line );
		vector<pair<size_t, size_t>> answer;

		int left = 0;
		int i = 0;
		while ( i < line.size() )
		{
			int suffix_found = -1;
			for ( size_t j = 0; j < suffixes.size(); j++ )
			{
				if ( line.substr ( i, suffixes[j].size() ) == suffixes[j] )
				{
					suffix_found = j;
					break;
				}
			}
			if ( suffix_found == -1 )
			{
				i++;
				continue;
			}
			else
			{
				int j = i - 1;
				i += suffixes[suffix_found].size();
				bool at_found = false;
				while ( j >= left )
				{
					if ( line[j] == '@' )
					{
						at_found = true;
						break;
					}
					if ( !IsValidSiteAddressChar ( line[j] ) )
					{
						break;
					}
					j--;
				}
				if ( !at_found )
				{
					continue;
				}
				else
				{
					// If the site address is empty
					if ( i - suffixes[suffix_found].size() - 1 == j )
					{
						continue;
					}
					else
					{
						int jBak = j;
						j--;
						while ( j >= left )
						{
							if ( !IsValidUserNameChar ( line[j] ) )
							{
								break;
							}
							j--;
						}
						j++;

						string userName = line.substr ( j, jBak - j );
						while ( jBak - j >= 5 && !IsValidUserName ( userName ) )
						{
							j++;
							userName = line.substr ( j, jBak - j );
						}

						if ( !IsValidUserName ( userName ) )
						{
							continue;
						}
						else
						{
							left = i;
							answer.push_back ( make_pair ( j, i - j ) );
						}
					}
				}
			}
		}

		cout << "Case #" << k++ << ": " << answer.size() << "\n";
		for ( size_t j = 0; j < answer.size(); j++ )
		{
			cout << line.substr ( answer[j].first, answer[j].second ) << "\n";
		}
	}
}
