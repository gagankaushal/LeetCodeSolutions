/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //IF BOTH TREES NULL
        //IF ONE OF THE TREE NULL BUT NOT THE OTHER
        //IF THE VALUE IS NOT SAME RETURN FALSE
        //THEN CHECK THE VALEU OF LEFT THEN RIGHT
        
        if (p == null && q == null){
            return true;
        }
        else if (p== null || q == null){
            return false;
        }
        
        else if (p.val != q.val) return false;
        
        return isSameTree(p.left,q.left) && isSameTree(p.right, q.right);
        
    }
}