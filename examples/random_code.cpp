// Program to illustrate the working of
// objects and class in C++ Programming

#include <iostream>
using namespace std;



// create a class
class root {

    public:
    double length;
    double breadth;
    double height;
};

class child : root {
    // fasd
}

class childchild : virtual child {
    //class here;
}

class childchildchild : public virtual childchild {
    /*
    class here2?;
    */
}

class anotherRoot;

class seconndchild : virtual protected root;


class yetanotherRoot {
    // asd
}

class childchildsequel : childchild {
    //asdasd
}

class childofsth : yetanotherRoot {
    public:
    int sth;
}