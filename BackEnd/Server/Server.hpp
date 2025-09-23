#pragma once

#include <iostream>

class Server{
    public:Server(){}
    public:~Server(){}
    public:void main(int argc, char* argv[]){
        int a,b;
        std::cin >> a >> b;
        std::cout << a+b << std::endl;
        while(true) std::cout<< a+b << std::endl;
    }
};
