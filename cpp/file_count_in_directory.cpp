#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>

#define BOOST_FILESYSTEM_NO_DEPRECATED
#include <boost/filesystem.hpp>

using namespace std;
using namespace boost::filesystem;

typedef unsigned long long ULL;

ULL ToULL( const string& str )
{
	stringstream ss( str );
	ULL ret;
	ss >> ret;
	return ret;
}

// Returns the number of files in the input directory
// The progress status is printed after every `milestone` files are visited.
// Here "file" refers to everything (regular_files, directories, symlinks etc.)
ULL GetNumberOfFiles( const path& inputPath = ".", const ULL& milestone = 1000 )
{
	ULL numberOfFiles = 0;

	if ( milestone == 0 )
	{
		numberOfFiles = std::distance( recursive_directory_iterator( inputPath ), recursive_directory_iterator() );
	}
	else
	{
		ULL filesVisitedIterator = 0;
		for ( recursive_directory_iterator it( inputPath ); it != recursive_directory_iterator(); ++it )
		{
			filesVisitedIterator++;
			if ( filesVisitedIterator == milestone )
			{
				numberOfFiles += filesVisitedIterator;
				filesVisitedIterator = 0;
				cout << "\rFiles visited = " << numberOfFiles << std::flush;
			}
		}

		numberOfFiles += filesVisitedIterator;
		if ( filesVisitedIterator )
		{
			cout << "\rFiles visited = " << numberOfFiles << std::flush;
		}

		cout << endl;
	}

	return numberOfFiles;
}

int main( int argc, char* argv[] )
{
	path inputPath = ".";
	ULL milestone = 1000;

	if ( argc > 1 )
	{
		inputPath = argv[1];
	}

	if ( argc > 2 )
	{
		milestone = ToULL( argv[2] );
	}

	try
	{
		cout << "Input path entered = " << inputPath << "\n";
		cout << "Input path resolved to = " << canonical( inputPath ) << "\n";
		cout << "Milestone = " << milestone << "\n\n";

		const auto numberOfFiles = GetNumberOfFiles( inputPath, milestone );
		print( numberOfFiles );
	}

	catch ( const filesystem_error& ex )
	{
		cout << ex.what() << '\n';
	}

	return 0;
}

