class Solution {
    static void preOrder(TreeNode root,List<Integer> res){
        if (root==null) return;
        res.add(root.val);
        preOrder(root.left,res);
        preOrder(root.right,res);
    }
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res=new ArrayList<>();
        preOrder(root,res);
        return res;
    }
}
