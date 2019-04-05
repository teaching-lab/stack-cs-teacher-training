use warnings;
use strict;

# a tree is just a nesteting of array references, each with 3 elements: value,
# left, right an empty tree has undefined value in root (therefore one must not
# insert undef into a tree)
sub empty {
    return [ undef, undef, undef ];
}

# insert given integral value into a tree
sub insert {
    my ( $val, $tree ) = @_;
    die "val must be defined in insert" if not defined $val;
    if ( not defined $tree->[0] ) {
        $tree->[0] = $val;
        return;
    }
    while ( 1 ) {
        my $pivot = $tree->[0];
        # note the int comparsion (compared to lt, string comparsion), the tree
        # can hold only integers
        my $id = $val < $pivot ? 1 : 2;
        if ( not defined $tree->[$id] ) {
            $tree->[$id] = [ $val, undef, undef ];
            return $tree;
        }
        else {
            $tree = $tree->[$id];
        }
    }
}

# check that given integral value is present in the tree
sub elem {
    my ( $val, $tree ) = @_;
    return 0 if not defined $tree->[0];
    return 0 if not defined $val;

    while ( defined $tree ) {
        my $pivot = $tree->[0];
        return 1 if $pivot == $val;
        $tree = $tree->[$val < $pivot ? 1 : 2];
    }
    return 0;
}

# https://rosettacode.org/wiki/Tree_traversal#Perl
sub inorder
{
    my $tree = shift or return ();
    return (inorder($tree->[1]), $tree->[0], inorder($tree->[2]));
}


# a simple test
my $tree = empty;
for my $v ( 5, 1, 3, 6, 7, 4, 25, 2, 15 ) {
    insert $v, $tree;
    print join( ", ", inorder $tree ) . "\n";
}

print "\n";

for my $v ( 1, 5, 9, 15, 17 ) {
    print "$v is " . (elem($v, $tree) ? "" : "not ") . "present in the tree\n";
}
