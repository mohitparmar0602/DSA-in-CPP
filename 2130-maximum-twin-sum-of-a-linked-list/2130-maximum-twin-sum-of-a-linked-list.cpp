/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> result;
        ListNode* current = head;
        while(current != nullptr){
            result.push_back(current->val);
            current = current->next;
        }
        int max_twin_sum = 0;
        int n = result.size();
        for(int i = 0; i < n / 2; i++){
            int twin_sum = result[i] + result[n - 1 - i];
            max_twin_sum = max(max_twin_sum, twin_sum);
        }
        return max_twin_sum;
    }
};