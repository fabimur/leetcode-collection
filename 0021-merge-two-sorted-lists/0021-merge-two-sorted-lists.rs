// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match(list1, list2){
            (None, r) => r,
            (l, None) => l,
            (Some(mut a), Some(mut b)) => {
                if a.val <= b.val {
                    a.next = Self::merge_two_lists(a.next.take(), Some(b));
                    Some(a)
                } else {
                    b.next = Self::merge_two_lists(Some(a), b.next.take());
                    Some(b)
                }
            }
        }
    }
}