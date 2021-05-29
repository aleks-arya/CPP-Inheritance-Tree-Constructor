// Program to illustrate the working of
// objects and class in C++ Programming

#include <iostream>
using namespace std;

class B;

// create a class
class A {

    public:
    double length;
    double breadth;
    double height;
};

class AA : A {
    public:
    int ree;
}

class BB : public B {
    int bb;
}

class BBB : private BB {
    int bbb;
}

class B : virtual public A{
    int b;
}

/*
class F
*/
class D;

class Badsf : protected virtual BB {
    // class ASD
}

class DD : D;

class DD2 : public D{
    //
}

class DDD : DD {
    
}

class D : AA {}