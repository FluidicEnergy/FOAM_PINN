/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) YEAR AUTHOR, AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "pointField.H"
#include "tensor.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 29 "/home/navier/Codes/PINN/FOAM_PINN/case/system/blockMeshDict/#codeStream"
#include "pointField.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C" void codeStream_123f85c96e12709e42dbeb6ffae52b95dd518b15(Foam::Ostream& os, const Foam::dictionary& dict)
{
//{{{ begin code
    #line 34 "/home/navier/Codes/PINN/FOAM_PINN/case/system/blockMeshDict/#codeStream"
pointField points(48);
points[0]  = point(0.5, 0, -0.5);
points[1]  = point(3, 0, -0.5);
points[2]  = point(25, 0, -0.5);
points[3]  = point(25, 0.353553, -0.5);
points[4]  = point(25, 3, -0.5);
points[5]  = point(25, 8, -0.5);
points[6]  = point(3, 8, -0.5);
points[7]  = point(3, 3, -0.5);
points[8]  = point(3, 0.353553, -0.5);
points[9]  = point(0.353553, 0.353553, -0.5);
points[10] = point(0.353553, 3, -0.5);
points[11] = point(0.353553, 8, -0.5);
points[12] = point(0, 8, -0.5);
points[13] = point(0, 3, -0.5);
points[14] = point(0, 0.5, -0.5);
points[15] = point(-0.5, 0, -0.5);
points[16] = point(-0.353553, 0.353553, -0.5);
points[17] = point(-0.353553, 3, -0.5);
points[18] = point(-0.353553, 8, -0.5);
points[19] = point(-3, 8, -0.5);
points[20] = point(-3, 3, -0.5);
points[21] = point(-3, 0.353553, -0.5);
points[22] = point(-3, 0, -0.5);
points[23] = point(-8, 0, -0.5);
points[24] = point(-8, 0.353553, -0.5);
points[25] = point(-8, 3, -0.5);
points[26] = point(-8, 8, -0.5);

points[27]  = point(25, -0.353553, -0.5);
points[28]  = point(25, -3, -0.5);
points[29]  = point(25, -8, -0.5);
points[30]  = point(3, -8, -0.5);
points[31]  = point(3, -3, -0.5);
points[32]  = point(3, -0.353553, -0.5);
points[33]  = point(0.353553, -0.353553, -0.5);
points[34] = point(0.353553, -3, -0.5);
points[35] = point(0.353553, -8, -0.5);
points[36] = point(0, -8, -0.5);
points[37] = point(0, -3, -0.5);
points[38] = point(0, -0.5, -0.5);
points[39] = point(-0.353553, -0.353553, -0.5);
points[40] = point(-0.353553, -3, -0.5);
points[41] = point(-0.353553, -8, -0.5);
points[42] = point(-3, -8, -0.5);
points[43] = point(-3, -3, -0.5);
points[44] = point(-3, -0.353553, -0.5);
points[45] = point(-8, -0.353553, -0.5);
points[46] = point(-8, -3, -0.5);
points[47] = point(-8, -8, -0.5);
// Duplicate z points
label sz = points.size();
points.setSize(2*sz);
for (label i = 0; i < sz; i++)
{
    const point& pt = points[i];
    points[i+sz] = point(pt.x(), pt.y(), -pt.z());
}


        os  << points;
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

