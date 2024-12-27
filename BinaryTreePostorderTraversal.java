class Solution {
    static void postOrder(TreeNode root,List<Integer> res){
        if(root==null) return;
        postOrder(root.left,res);
        postOrder(root.right,res);
        res.add(root.val);
    }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res=new ArrayList<>();
        postOrder(root,res);
        return res;
    }
}
