/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNodes(struct ListNode* head) {
    struct ListNode *temp1=head;
    int n=0;
    while(temp1!=NULL){
        n++;
        temp1=temp1->next;
    }
    int arr[n];
    temp1=head;
    int i=0;
    while(temp1!=NULL){
        arr[i]=temp1->val;
        i++;
        temp1=temp1->next;
    }
    i+=-1;
    int max=arr[i];
    while(i>=0){
        if(max<=arr[i]) max=arr[i];
        else arr[i]=0;
        i+=-1;
    }
    temp1=head;
    struct ListNode *temp2=head;
    i=0;
    while(temp1!=NULL){
        if (temp1==head){
            if(arr[i]==0){
                head=head->next;
                free(temp1);
                temp1=head;
                temp2=head;
            }
            else{
                temp1=temp1->next;
            }
        }
        else{
            if (arr[i]==0){
                temp2->next=temp1->next;
                free(temp1);
                temp1=temp2->next;
            }
            else{
                temp2=temp1;
                temp1=temp1->next;
            }
        }
        i++;
    }
    return head;
}
