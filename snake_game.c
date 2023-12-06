#include <iostream>
using namespace std;

class Line {
    public:
        double length;
        void setLen(double len);
        double getLen(void);
};

double Line::getLen(void){
    return length;
}
void Line::setLen(double len){
    length=len;
}
int main(){
    Line line;
    line.setLen(6.0);
    cout<<"Length of line:"<<line.getLen()<<endl;
    line.length=10.0;
    cout<<"Length of line:"<<line.length<<endl;
    return 0;
}