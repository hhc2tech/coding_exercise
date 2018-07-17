#include<unordered_map>
#include<vector>
#include<stack>
#include <iostream>
#include<queue> 

using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};


ListNode* buildLinkedList(vector<int> A){
    ListNode dummy(INT_MIN);
    ListNode *head = &dummy;

    if (A.size() == 0) return NULL; 
    for (int i = 0; i < A.size(); i++){
        head->next = new ListNode(A[i]);
        head = head->next;
    }
    return dummy.next;
}


void printLinkedlist(ListNode* head){
    if (head == NULL){ 
        cout<<"Empty list!\n";
        return;
    }
    while (head != NULL){
        cout<<head->val<<"->"; 
        head = head->next; 
    }
    cout<<"NULL";
    return;
}

ListNode* reverseList(ListNode* head){
    ListNode* prev(NULL); 
    while (head != NULL){
        ListNode* next = head->next; 
        head->next = prev;
        prev = head; 
        head = next; 
    }
    return prev; 
}

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    /* merge two sorted list
    */
   if (!l1) return l2; 
   if (!l2) return l1; 
   ListNode dummy(INT_MIN); 
   ListNode* head = &dummy; 
   while (l1 && l2){
       if (l1->val < l2->val){
           head->next = l1; 
           l1 = l1->next;
       }
       else{
           head->next = l2; 
           l2 = l2->next;
       }
       head = head->next; 
   }
   head->next = l1? l1:l2;
   return dummy.next;
}



void test_mergeTwoLists(){
    vector<int>A = {1, 4, 5}; 
    vector<int>B = {2, 6, 7}; 
    ListNode* l1 = buildLinkedList(A); 
    ListNode* l2 = buildLinkedList(B); 
    printLinkedlist(l1);
    cout<<"+";
    printLinkedlist(l2); 
    cout<<"=";
    printLinkedlist(mergeTwoLists(l1, l2)); return; 
}

bool isPalindrome(ListNode* head){
    if (!head) return true;
    ListNode* slow = head; 
    ListNode* fast = head; 
    ListNode* prev(NULL);
    while (fast && fast->next){
        fast = fast->next->next; 
        ListNode* next = slow->next; 
        slow->next = prev; 
        prev = slow; 
        slow = next; 
    }
    if (fast) slow = slow->next; 
    while (slow){
        if (slow->val != prev->val) return false; 
        slow = slow->next; 
        prev = prev->next;
    }
    return true; 
}

void test_isPalindrome(){
    vector<int> vect1 = {1};
    vector<int> vect2 = {1, 2, 1}; 
    vector<int> vect3 = {1, 2, 2, 1}; 
    vector<int> vect4 = {1, 2, 3, 3, 3, 1}; 
    ListNode * head1 = buildLinkedList(vect1);
    ListNode * head2 = buildLinkedList(vect2);
    ListNode * head3 = buildLinkedList(vect3);
    ListNode * head4 = buildLinkedList(vect4);

    cout<<"\nIs "; printLinkedlist(head1); 
    cout<<" palindrom? "<<isPalindrome(head1);
    cout<<"\nIs "; printLinkedlist(head2); 
    cout<<" palindrom? "<<isPalindrome(head2);

    cout<<"\nIs "; printLinkedlist(head3); 
    cout<<" palindrom? "<<isPalindrome(head3);

    cout<<"\nIs "; printLinkedlist(head4); 
    cout<<" palindrom? "<<isPalindrome(head4);
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode dummy(0); 
    ListNode* head = &dummy; 
    int carry = 0; 
    while (l1 || l2 || carry){
        if (l1){
            carry += l1->val; 
            l1 = l1->next;
        } 
        if (l2){
            carry += l2->val; 
            l2 = l2->next;
        }
        head->next = new ListNode(carry%10);
        head = head->next; 
        carry /=10;
    }
    return dummy.next; 
}

void test_addTwoNumbers(){
    vector<int> vect2 = {9, 9}; 
    vector<int> vect1 = {1};
    ListNode* l1 = buildLinkedList(vect1);
    ListNode* l2 = buildLinkedList(vect2); 
    printLinkedlist(l1); 
    cout<<endl;
    printLinkedlist(l2); 
    cout<<endl; 
    printLinkedlist(addTwoNumbers(l1, l2));
}

void print_vector(vector<int> A){
    if (A.size() == 0) {
        cout<< "emtpy vector";
        return; 
        }
    cout<<"[";
    for (int i = 0; i < A.size() - 1; i++) cout<<A[i]<<", ";
    cout<<A[A.size() - 1]<<"]";
    // cout<<endl;

}

void print_vector(vector<vector<int>> A){
    int M = A.size(); 
    if (M == 0|| A[0].size() == 0) {
        cout<<"[[]]\n";
        return;
    }
    // first row 
    cout<<"\n[";
    print_vector(A[0]); 
    for (int i = 1; i < M; i++) {
        cout<<"\n "; 
        print_vector(A[i]); 
    }
    cout<<"]";
}

void test_vector(){
    // initializations 
    // 
    cout<<"Initialization\n";
    vector<int> vect1 = {1, 2, 3}; 
    vector<int> vect2(5, 1); 
    vector<int> vect3 = vect1; 
    vector<int> vect4 = {100, 101, 1002}; 

    cout<<"vector 1: "; print_vector(vect1); 
    cout<<"\nvector 2: "; print_vector(vect2);  
    cout<<"\nvector 3: "; print_vector(vect3);  

    // insert one element 
    cout<<"\nInsert one element\n";
    vect1.insert(vect1.begin(), 100); 
    cout<<"\nvector 1: "; print_vector(vect1); 
    vect2.insert(vect2.begin()+2, 10);
    cout<<"\nvector 2: "; print_vector(vect2);  

    // delete one element 
    cout<<"\nErase (delete) one element\n"; 
    vect1.erase(vect1.begin()); 
    cout<<"\nvector 1: "; print_vector(vect1); 
    //clear vector
    vect3.clear(); 
    cout<<"\nvector 3: "; print_vector(vect3);  
    

    // concatenate two vector 
    // easy way 
    cout<<"\nConcatenating two vectors\n";
    for (int n: vect2) vect1.push_back(n); 
    cout<<"\nvector 1: "; print_vector(vect1); 
    //
    vect2.insert(vect2.end(), vect4.begin(), vect4.end()); 
    cout<<"\nvector 2: "; print_vector(vect2);  
    vect4.insert(vect4.begin() + 1, vect1.begin(), vect1.end()); 
    cout<<"\nvector 4: "; print_vector(vect4); 

    // find an element in a vector 
    auto it = find(vect4.begin(), vect4.end(), 10);
    if (it != vect4.end()) cout<<it - vect4.begin()<<endl; 

    /// vector of vector 
    vector<vector<int>> A = {{1, 2}, {3, 4}}; 
    vector<vector<int>> B = {{1}}; 
    vector<vector<int>> C = {{}}; 
    cout<<"\nA: "; print_vector(A); 
    cout<<"\nB: "; print_vector(B); cout<<endl;
    cout<<"C: "; print_vector(C); cout<<endl; 
}

// TODO: working with strings 
void test_string(){
    string a = "aaa"; 
    cout<<a<<endl; 
    for(auto c: a) cout<<c; 
    string b = "vu huu tiep."; 
    auto i = find(b.begin(), b.end(), 'u');
    cout<<(i - b.begin())<<endl; 

    // concatenate two strings 
    cout<<a + b<<endl; 
    a.append(10, 'u'); //append 10 'u' into a  
    cout<<a; 
}

// TODO: working with queues 
void print_queue(queue<int> q){
    while (!q.empty()){
        cout<<q.front()<<" ";
        q.pop();
    }
}
void test_queue(){
    queue<int> A; 
    vector<int> b = {1, 2, 3};
    for (auto n: b) A.push(n); 
    print_queue(A); 

}
// TODO: working with stacks 

// TODO: working with hash map, map, unordered_map 


vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size(); 
        vector<vector<int>> res = {{}}; 
        
        if (n == 0) return res; 
        for (int i = 0; i < n; i++){
            vector<vector<int>> tmp; 
            for (vector<int> per:res){
                for (int j =0; j < i+1; j++){
                    vector<int> new_per = per;
                    if (j < i) new_per.insert(new_per.begin()+j, nums[i]);
                    else new_per.insert(new_per.end(), nums[i]); 
                    tmp.push_back(new_per); 
                }
            }
            res = tmp; 
        }
        return res; 
    }

void test_permute(){ 
    vector<int> nums = {1, 2, 3}; 
    vector<vector<int>> res = permute(nums); 
    print_vector(res); 
}


void nextPermutation(vector<int>& nums) {
    /*find the next permutation, return in-place 
    Implement next permutation, which rearranges numbers into the 
    lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest 
    possible order (ie, sorted in ascending order).
    The replacement must be in-place and use only constant extra memory.
    Here are some examples. Inputs are in the left-hand column and its 
    corresponding outputs are in the right-hand column.
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    */
    }


int main() {
    // vector<int> A = {1, 2, 3, 4};
    // ListNode* head = buildLinkedList(A); 
    // printLinkedlist(head);
    // printLinkedlist(reverseList(head));
    // test_mergeTwoLists();
    // test_isPalindrome();
    // test_addTwoNumbers();
    // test_vector(); 
    // test_string(); 
    // test_queue(); 
    test_permute(); 
    return 0;
}
