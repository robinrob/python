


void top_view(Node root)
{
        if (root.left != null) {
            top_view_left(root.left);
        }

        System.out.format("%d ", root.data);

        if (root.right != null) {
            top_view_right(root.right);
        }
}


void top_view_left(Node root)
{
        if (root.left != null) {
            top_view_left(root.left);
        }

        System.out.format("%d ", root.data);
}

void top_view_right(Node root)
{
        System.out.format("%d ", root.data);

        if (root.right != null) {
            top_view_right(root.right);
        }
}