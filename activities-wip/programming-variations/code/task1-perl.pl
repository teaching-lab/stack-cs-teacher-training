sub empty {
    #      [ value, left , right ]
    return [ undef, undef, undef ];
}

sub insert {
    my ( $val, $tree ) = @_;
    die "val must be defined in insert" if not defined $val;
    if ( not defined $tree->[ 0 ] ) {
        $tree->[ 0 ] = $val;
        return;
    }
    while ( 1 ) {
        my $pivot = $tree->[ 0 ];
        my $id = $val < $pivot ? 1 : 2;
        if ( not defined $tree->[ $id ] ) {
            $tree->[ $id ] = [ $val, undef, undef ];
            return $tree;
        }
        else {
            $tree = $tree->[ $id ];
        }
    }
}

sub lookup {
    my ( $val, $tree ) = @_;
    return 0 if not defined $tree->[ 0 ];
    return 0 if not defined $val;

    while ( defined $tree ) {
        my $pivot = $tree->[ 0 ];
        return 1 if $pivot == $val;
        $tree = $tree->[ $val < $pivot ? 1 : 2 ];
    }
    return 0;
}
