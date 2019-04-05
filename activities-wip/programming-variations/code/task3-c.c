#include<stdio.h>
#include<stdlib.h>
  
struct node {
    int data;
    struct node* left;
    struct node* right;
};

struct node* createNode(value){
    struct node* newNode = malloc(sizeof(struct node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
  
struct node* insert(struct node* root, int data)
{
    if (root == NULL) return createNode(data);
    if (data < root->data)
        root->left  = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);   
    return root;
}

void printInorder(struct node* root){
    if (root == NULL) return;
    printInorder(root->left);
    printf("%d - ", root->data);
    printInorder(root->right);
}

int main() {
    struct node* tree = NULL;
    tree = insert(tree, 5); tree = insert(tree, 4);
    tree = insert(tree, 2); tree = insert(tree, 8);
    printInorder(tree);
}
