#include "fvCFD.H"
#include "timeSelector.H"

int main(int argc, char *argv[])
{
    argList::noParallel();
    timeSelector::addOptions();

    #include "setRootCase.H"
    #include "createTime.H"

    instantList runTimes = timeSelector::select0(runTime, args);
    runTime.setTime(runTimes[0], 0);

    #include "createMesh.H"

    Info << "Reading U and p fields at time = " << runTime.timeName() << endl;

    volVectorField U
    (
        IOobject
        (
            "U",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

    volScalarField p
    (
        IOobject
        (
            "p",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

    const volVectorField& cellCenters = mesh.C();

    fileName outputDir(runTime.timeName());
    mkDir(outputDir);

    //  통합 파일로 저장
    OFstream outputFile(outputDir / "U_p_points.dat");

    forAll(U, cellI)
    {
	const vector& pt = cellCenters[cellI];
        const vector& vel = U[cellI];
        scalar pressure = p[cellI];

        outputFile 
            << pt.x() << " " << pt.y() << " " << pt.z() << " "
            << vel.x() << " " << vel.y() << " " << vel.z() << " "
            << pressure << endl;
    }

    Info << "Merged U+p extraction complete." << endl;
    return 0;
}
