#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <random>
#include <set>
#include <tuple>
#include <utility>
#include <vector>
#include <stdlib.h>
#include <ctime>

// ------------------------------------------------------------------------
class Point
{
  friend std::ostream& operator<<( std::ostream& o, const Point& p )
  {
    o << p.X << "," << p.Y ;
    return( o );
  }
public:
  Point( )
    : X( 0 ),
      Y( 0 )
  {
    if( Point::Device == NULL )
      Point::Device = new std::random_device( );
    if( Point::Generator == NULL )
      Point::Generator = new std::mt19937( ( *Point::Device )( ) );
    if( Point::Distribution == NULL )
      Point::Distribution = new std::uniform_real_distribution<>( -1000, 1000 );
  }
  double X;
  double Y;

  virtual ~Point( )
  {
  }

  void RandomFill( )
  {
    this->X = ( *Point::Distribution )( *Point::Generator );
    this->Y = ( *Point::Distribution )( *Point::Generator );
  }

  bool operator<( const Point& b ) const
  {
    if( this->X == b.X )
      return( this->Y < b.Y );
    else
      return( this->X < b.X );
  }

  double DistanceTo( const Point& b ) const
  {
    double d = ( this->X - b.X ) * ( this->X - b.X );
    d       += ( this->Y - b.Y ) * ( this->Y - b.Y );
    return( std::sqrt( d ) );
  }

protected:
  static std::random_device* Device;
  static std::mt19937* Generator;
  static std::uniform_real_distribution<>* Distribution;
};

std::random_device* Point::Device = NULL;
std::mt19937* Point::Generator = NULL;
std::uniform_real_distribution<>* Point::Distribution = NULL;

// ------------------------------------------------------------------------
typedef std::set< Point >                TPointSet;
typedef std::vector< Point >             TPoints;
typedef std::multimap< double, TPoints > TPointMap;
typedef std::pair< double, TPoints >     THamiltonLoop;
typedef std::vector< long >              TMST;

// ------------------------------------------------------------------------
THamiltonLoop Hamilton_BF( const TPoints& points );
THamiltonLoop Hamilton_Dijkstra( const TPoints& points );

// ------------------------------------------------------------------------
TMST Dijkstra( const TPoints& points, long seed );

// ------------------------------------------------------------------------
int main( int argc, char* argv[] )
{
  //Codigo que genera los 100 grafos aleatorios
  /*std::ofstream out_file;
  out_file.open("bf_costs.txt");
  for (int k = 1;k<=100;k++){
    TPointSet point_set;
    while( point_set.size( ) < 8 )
    {
      Point p;
      p.RandomFill( );
      point_set.insert( p );

    } // end while
    TPoints points( point_set.begin( ), point_set.end( ) );

    //std::cout << "-------------------------------" << std::endl;
    //std::cout << "Points" << std::endl;
    std::ofstream file;
    std::string name = "graph"+std::to_string(k)+".txt"; 
    file.open(name);
    for( const Point& p: points ){
      file << p << std::endl;
    }
    file.close();
  }*/

  std::ofstream out_file_time;
  out_file_time.open("bf_times.txt");
  for(int i = 1;i<=100;i++){
    std::string name = "graph"+std::to_string(i)+".txt"; 
    std::fstream file (name);
    std::string line;
    TPointSet point_set;
    if(file.is_open()){
      while(getline(file,line)){
        Point p;
        std::string del = ",";
        std::string tok = line.substr(0,line.find(del));
        p.X = std::stod(tok);
        line.erase(0, line.find(del)+del.length());
        p.Y = std::stod(line);
        point_set.insert( p );
      }
    }
    file.close();
    TPoints points( point_set.begin( ), point_set.end( ) );
    int start_s=clock();
    THamiltonLoop hl_bf = Hamilton_BF( points );
    int stop_s=clock();
    out_file_time <<(stop_s-start_s)/double(CLOCKS_PER_SEC)*1000 << std::endl;
    std::cout << "-------------------------------" << std::endl;
    std::cout << "Brute Force" << std::endl;
    std::cout << "Cost: " << hl_bf.first << std::endl;
    //out_file << hl_bf.first << std::endl;
    std::cout << "Loop:";
    for( const Point& p: hl_bf.second )
      std::cout << " " << p;
    std::cout << std::endl << "-------------------------------" << std::endl;
  }
  out_file_time.close();
  //out_file.close();

}

THamiltonLoop Hamilton_BF( const TPoints& points )
{
  TPoints perm( points.begin( ), points.end( ) );
  TPointMap all_options;
  while( std::next_permutation( perm.begin( ), perm.end( ) ) )
  {
    double c = 0;
    for( unsigned int i = 0; i < perm.size( ); ++i )
      c += perm[ i ].DistanceTo( perm[ ( i + 1 ) % perm.size( ) ] );
    all_options.insert( THamiltonLoop( c, perm ) );
  } // end while
  return( *( all_options.begin( ) ) );
}

// ------------------------------------------------------------------------