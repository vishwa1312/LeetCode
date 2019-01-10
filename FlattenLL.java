class Solution {
    private Node pre = null;
public Node flatten(Node head) {
    helper(head);
    return head;
}

private void helper(Node cur) {
    if (cur == null) return;
    helper(cur.next);
    helper(cur.child);
    cur.next = pre;
    if (pre != null) {
        pre.prev = cur;
    }
    pre = cur;
    cur.child = null;
}
}
