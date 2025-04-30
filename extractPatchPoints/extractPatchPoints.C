#include "fvCFD.H"
#include "volFields.H"

int main(int argc, char *argv[])
{
    argList::noParallel();
    #include "setRootCase.H"
    #include "createTime.H"
    #include "createMesh.H"

    const polyBoundaryMesh& boundaries = mesh.boundaryMesh();

    forAll(boundaries, patchI)
    {
        const polyPatch& patch = boundaries[patchI];
        const labelList& patchPoints = patch.meshPoints();
	
	fileName outputDir("0");
	mkDir(outputDir);  // 0 디렉토리가 없으면 생성
	fileName outputName = outputDir / (patch.name() + "_points.dat");
        Info << "Writing patch " << patch.name() << " to " << outputName << endl;

        OFstream outputFile(outputName);

        forAll(patchPoints, i)
        {
            const point& pt = mesh.points()[patchPoints[i]];
            outputFile << pt.x() << " " << pt.y() << " " << pt.z() << endl;
        }
    }

    Info << "Patch points extracted." << endl;
    return 0;
}
