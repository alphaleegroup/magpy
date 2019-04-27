Information about elemental property lookup tables. Most of this data was taken from Mathematica's elemental property data (sources described at http://reference.wolfram.com/mathematica/note/ElementDataSourceInformation.html). Modifications and, when not from Mathematica, original sources are listed.


AtomicVolume
* Property: Volume of an atom of each element
* Units: A^3 / atom
* Source: Derived from atomic weight and density AtomicVolume = AtomicWeight / Density

AtomicWeight
* Property: Atomic weight

BulkModulus
* Property: Bulk modulus
* Units: GPa
* Source: Mathematica

BoilingT
* Property: Boiling temperature
* Units: K
* Source: Mathematica

Column
* Property: Column on periodic table
* Notes: Column of all RE elements is listed as 3

CovalentRadius
* Property: Covalent radius of each element <In where, whose assessment?>
* Units: pm
* Source: Mathematica

Density
* Property: Density of element at STP
* Units: g/L
* Source: Mathematica

ElectronAffinity
* Property: Electron affinitiy
* Units: kJ/mol
* Source: Mathematica

Electronegativity
* Property: Pauling electronegativity (right?)
* Source: Mathematica
* Notes: Eu electronegativity to 1.185 (average of neighbors), Yb electronegativity to 1.26 (average of neighbors), Tb electronegativity set to 1.21 (average of neighbors), Pm electronegativity set to 1.155 (average of neighbors)

FirstIonizationEnergy
* Property: Energy to remove the first electron from an element
* Units: eV
* Source: CRC Handbook

GSbandgap
* Property: DFT bandgap energy of T=0K ground state
* Units: eV
* Source: OQMD

GSestBCClatcnt
* Property: Estimated BCC lattice parameter based on the DFT volume of the OQMD ground state for each element

HeatCapacityMass
* Property: Specific heat capacity at STP
* Units: J/g-K
* Source: CRC Handbook

HeatCapacityMolar
* Property: Molar heat capacity at STP
* Units: J/mol-K
* Source: CRC Handbook
* Units: Angstrom
* Source: OQMD

HeatFusion
* Property: Enthalpy of fusion for elements at their melting temperatures
* Units: kJ/mol
* Source: CRC Handbook
* Notes: Heat of fusion are listed per diatomic molecule for appropriate elements, we computed per mole of atoms (i.e., divided listed value by 2)

GSestFCClatcnt
* Property: Estimated FCC lattice parameter based on the DFT volume of the
OQMD ground state for each element
* Units: Angstrom
* Source: OQMD

GSenergy_pa
* Property: DFT energy per atom (raw VASP value) of T=0K ground state
* Units: eV/atom
* Source: OQMD

GSmagmom
* Property: DFT magnetic momenet of T=0K ground state
* Source: OQMD

GSvolume_pa
* Property: DFT volume per atom of T=0K ground state
* Units: Angstrom^3/atom
* Source: OQMD

HHIp
* Property: Herfindahl−Hirschman Index (HHI) production values
* Source: Gaultois et al., 2013. http://pubs.acs.org/doi/abs/10.1021/cm400893e

HHIr
* Property: Herfindahl−Hirschman Index (HHI) reserves values
* Source: Gaultois et al., 2013. http://pubs.acs.org/doi/abs/10.1021/cm400893e

ICSDVolume
* Property: Volume per atom of ICSD phase at STP
* Source: Inorganic Crystal Structure Database

IsAlkali
* Property: Whether an element is an alkali or alkali earth metal

IsDBlock
* Property: Whether an element is a d-block metal

IsFBlock
* Property: Whether an element is an f-block metal

IsMetal
* Property: Whether an element is a metal

IsMetalloid
* Property: Whether an element is a metalloid

IsNonmetal
* Property: Whether an element is a nonmetal

MeltingT
* Property: Melting temperature of element
* Units: K
* Source: Mathematica

MendeleevNumber
* Property: Mendeleev Number (position on the periodic table, counting columnwise from H)
* Source: Villars et al., 2004. http://linkinghub.elsevier.com/retrieve/pii/S0925838803008004

MiracleRadius
* Property: Assessed radii of elements in metallic glass structures
* Units: pm
* Source: Miracle et al., 2010. doi:10.1179/095066010X12646898728200

NdUnfilled
* Property: Number of unfilled d valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html
* Notes: Number of unoccupied orbitals = 0 if shell unoccupied, Maximum-Filled if occupied

NdValence
* Property: Number of filled d valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html

NfUnfilled
* Property: Number of unfilled f valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html
* Notes: Number of unoccupied orbitals = 0 if shell unoccupied, Maximum-Filled if occupied

NfValence
* Property: Number of filled f valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html

NpUnfilled
* Property: Number of unfilled p valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html
* Notes: Number of unoccupied orbitals = 0 if shell unoccupied, Maximum-Filled if occupied

NpValence
* Property: Number of filled p valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html

NsUnfilled
* Property: Number of unfilled s valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html
* Notes: Number of unoccupied orbitals = 0 if shell unoccupied, Maximum-Filled if occupied

NsValence
* Property: Number of filled p valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html

Number
* Property: Atomic number

NUnfilled
* Property: Number of unfilled valence orbitals
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html
* Notes: Number of unoccupied orbitals = 0 if shell unoccupied, Maximum-Filled if occupied

NValance
* Property: Number of valence electrons
* Source: http://periodictable.com/Properties/A/ElectronConfigurationString.v.html

Polarizability
* Property: Static average electric dipole polarizability
* Units: 10^-24 cm^3
* Source: CRC Handbook

phi
* Property: Adjusted work function (used in the Miedema's model)
* Units: eV
* Source: Cohesion in metals: transition metal alloys, (North-Holland, Amsterdam, 1988)

Row
* Property: Row on periodic table

ShearModulus
* Property: Shear modulus
* Units: GPa
* Source: Mathematica
* Notes: Mn shear modulus from: http://www.azom.com/properties.aspx?ArticleID=1699

SpaceGroupNumber
* Property: Space group of T=0K ground state structure
* Source: Only structures from the ICSD were evaluated, Pm used OQMD groundstate in Spacegroup 194, which is only 4 meV/atom below 166. No ICSD structure

Wigner
* Property: Electron density at surface of Wigner-Sietz cell. Used in Miedema's model
* Source: Cohesion in metals: transition metal alloys, (North-Holland, Amsterdam, 1988)

ZungerPP-r_s
* Property: Psuedopotential radius of s orbital
* Units: a.u.
* Source: http://link.aps.org/doi/10.1103/PhysRevB.22.5839

ZungerPP-r_p
* Property: Psuedopotential radius of p orbital
* Units: a.u.
* Source: http://link.aps.org/doi/10.1103/PhysRevB.22.5839

ZungerPP-r_d
* Property: Psuedopotential radius of d orbital
* Units: a.u.
* Source: http://link.aps.org/doi/10.1103/PhysRevB.22.5839

ZungerPP-r_sigma
* Property: Sum of the radii of s and p orbitals
* Units: a.u.
* Source(s): http://link.aps.org/doi/10.1103/PhysRevB.22.5839; http://linkinghub.elsevier.com/retrieve/pii/0022508885901109

ZungerPP-r_pi
* Property: Absolute value of the different between the radii of s and p orbitals
* Units: a.u.
* Source: http://link.aps.org/doi/10.1103/PhysRevB.22.5839
