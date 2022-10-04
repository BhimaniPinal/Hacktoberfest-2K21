#include <bits/stdc++.h>

using namespace std;

struct Node{
    int val;
    struct Node *next;
};

// typedef Node* nodeptr;


Node *head = NULL;

void insert(int data){
    Node *newNode = new Node;
    newNode->val = data;
    newNode->next = head;
    head = newNode;
}

struct Node* findMiddle(){
    Node* slowptr = head;
    Node* fastptr = head;

    while(fastptr && fastptr->next){
        slowptr = slowptr->next;
        fastptr = fastptr->next->next;
    }
    return slowptr;
}

void display(){
    Node *curNode = head;
    while (curNode != NULL){
        cout << curNode->val << " ";
        curNode = curNode->next;
    }
    cout << "\n";
}

int main(){
    insert(5);
    insert(10);
    insert(20);
    insert(25);
    insert(30);
    display();
    Node* mid = findMiddle();
    cout << mid->val << endl;
    return 0;
}