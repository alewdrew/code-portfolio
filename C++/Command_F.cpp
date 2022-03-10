#include <iostream>
#include <unordered_map>
#include <string>

class command {
public:
    std::unordered_map<std::string,std::string> review;
    std::string EnterCon;
    std::string QorC;
};

int main() {
    command myObj;

    //Chapter One

//Q One
    myObj.review = {{"Question","D: Answer"},
    };
    std::cout << "(Enter 'quit' to end.)";

    for ( ; ; ) {

            myObj.QorC = "\nEnter question: ";
            std::cout << myObj.QorC;
            getline(std::cin, myObj.EnterCon);
            auto got = myObj.review.find(myObj.EnterCon);

                if (got == myObj.review.end()) {
                    std::cout << "not found";
                }
                else
                    std::cout << "Answer: " << got->second;
                if (myObj.EnterCon == "quit")
                    return 0;
}}
