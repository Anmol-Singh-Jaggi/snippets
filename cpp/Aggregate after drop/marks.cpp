#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define fastin std::ios::sync_with_stdio(false);cin.tie(nullptr)
#define cout_precision(x) cout<<std::fixed<<setprecision(x)
using namespace std;

typedef long long LL;

// Magic; kindly do not touch
// Generate the lowest number bigger than "bitmask" having exactly "r" set bits
void Advance( LL& bitMask )
{
	assert( bitMask > 0 );

	LL var1 = bitMask & ~( bitMask - 1 );
	LL var2 = ( bitMask + var1 ) & ~bitMask;

	bitMask |= var2;
	bitMask &= ~( var2 - 1 );
	bitMask |= ( ( var2 / var1 ) >> 1 ) - 1;
}

vector<LL> GenerateSubsets( const size_t& n, const size_t& r )
{
	assert( n > 0 );
	assert( r > 0 );
	assert( n >= r );

	vector<LL> subsets;

	// The smallest number having exactly "r" bits set
	// The set bits in the binary of "bitMask" denote the positions of the set included in the subset
	LL bitMask = ( 1LL << r ) - 1;
	subsets.push_back( bitMask );

	// This loop should run exactly nCr times
	while ( 1 )
	{
		Advance( bitMask );

		if ( bitMask & ( 1LL << n ) )
		{
			break;
		}

		subsets.push_back( bitMask );
	}

	return subsets;
}

// Extracts the subset indices from the bitmask
vector<size_t> DecodeMask( LL bitMask )
{
	vector<size_t> positions;

	size_t i = 0;

	while ( bitMask )
	{
		if ( bitMask & 1 )
		{
			positions.push_back( i );
		}
		bitMask >>= 1;
		i++;
	}

	return positions;
}


class Subject
{
public:

	string code;
	size_t credits;
	size_t marksTotal;
	size_t marksObtained;

	Subject( const string& _code = "xxx", const size_t& _credits = 0, const size_t& _marksTotal = 0, const size_t& _marksObtained = 0 )
	{
		code = _code;
		credits = _credits;
		marksTotal = _marksTotal;
		marksObtained = _marksObtained;
	}

};

Subject ReadSubject()
{
	Subject subject;

	string line;
	while ( getline( cin, line ) )
	{
		if ( line.empty() )
		{
			continue;
		}
		stringstream ss( line );

		ss >> subject.code;
		ss >> subject.credits;
		ss >> subject.marksTotal;
		ss >> subject.marksObtained;
		break;
	}

	return subject;
}

ostream& operator <<( std::ostream& out, const Subject& subject )
{
	out << "( " << subject.code << ", " << subject.credits << ", " << subject.marksTotal << ", " << subject.marksObtained << " )";
	return out;
}

double MaxAfterDrop( const vector<Subject>& subjects )
{
	size_t numerator = 0, denominator = 0;
	for ( size_t i = 0; i < subjects.size(); i++ )
	{
		numerator += subjects[i].marksObtained * subjects[i].credits;
		denominator += subjects[i].marksTotal * subjects[i].credits;
	}

	double maxAggregate = ( double )numerator / denominator;
	vector<size_t> ansIndex;

	const auto& subsets = GenerateSubsets( subjects.size(), 3 );
	for ( size_t i = 0; i < subsets.size(); i++ )
	{
		const vector<size_t> dropIndex = DecodeMask( subsets[i] );
		for ( size_t j = 0; j < dropIndex.size(); j++ )
		{
			const size_t index = dropIndex[j];
			numerator -= subjects[index].marksObtained * subjects[index].credits;
			denominator -= subjects[index].marksTotal * subjects[index].credits;
		}

		double aggregate = ( double )numerator / denominator;
		if ( aggregate > maxAggregate )
		{
			maxAggregate = aggregate;
			ansIndex = dropIndex;
		}

		for ( size_t j = 0; j < dropIndex.size(); j++ )
		{
			const size_t index = dropIndex[j];
			numerator += subjects[index].marksObtained * subjects[index].credits;
			denominator += subjects[index].marksTotal * subjects[index].credits;
		}
	}

	cout << "\n\nThe dropped subjects are -:\n\n";
	for ( size_t i = 0; i < ansIndex.size(); i++ )
	{
		const size_t index = ansIndex[i];
		cout << subjects[index] << "\n";
	}
	cout << "\n";

	return maxAggregate;
}

int main()
{
	vector<Subject> subjects;

	while ( 1 )
	{
		Subject subject = ReadSubject();
		if ( subject.code == "xxx" )
		{
			break;
		}
		subjects.push_back( subject );
	}

	cout << "Max aggregate = " << MaxAfterDrop( subjects ) * 100 << endl;
}
