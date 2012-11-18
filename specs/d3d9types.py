##########################################################################
#
# Copyright 2011 Jose Fonseca
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""d3d9types.h"""

from winapi import *

D3DCOLOR = Alias("D3DCOLOR", DWORD)

D3DVECTOR = Struct("D3DVECTOR", [
    (Float, "x"),
    (Float, "y"),
    (Float, "z"),
])

D3DCOLORVALUE = Struct("D3DCOLORVALUE", [
    (Float, "r"),
    (Float, "g"),
    (Float, "b"),
    (Float, "a"),
])

D3DRECT = Struct("D3DRECT", [
    (LONG, "x1"),
    (LONG, "y1"),
    (LONG, "x2"),
    (LONG, "y2"),
])

D3DMATRIX = Struct("D3DMATRIX", [
    (Array(Array(Float, 4), "4"), "m"),
])

D3DVIEWPORT9 = Struct("D3DVIEWPORT9", [
    (DWORD, "X"),
    (DWORD, "Y"),
    (DWORD, "Width"),
    (DWORD, "Height"),
    (Float, "MinZ"),
    (Float, "MaxZ"),
])

D3DCLIPPLANE = Flags(DWORD, [
    "D3DCLIPPLANE0",
    "D3DCLIPPLANE1",
    "D3DCLIPPLANE2",
    "D3DCLIPPLANE3",
    "D3DCLIPPLANE4",
    "D3DCLIPPLANE5",
])

D3DCS = Flags(DWORD, [
    "D3DCS_ALL",
    "D3DCS_LEFT",
    "D3DCS_RIGHT",
    "D3DCS_TOP",
    "D3DCS_BOTTOM",
    "D3DCS_FRONT",
    "D3DCS_BACK",
    "D3DCS_PLANE0",
    "D3DCS_PLANE1",
    "D3DCS_PLANE2",
    "D3DCS_PLANE3",
    "D3DCS_PLANE4",
    "D3DCS_PLANE5",
])

D3DCLIPSTATUS9 = Struct("D3DCLIPSTATUS9", [
    (DWORD, "ClipUnion"),
    (DWORD, "ClipIntersection"),
])

D3DMATERIAL9 = Struct("D3DMATERIAL9", [
    (D3DCOLORVALUE, "Diffuse"),
    (D3DCOLORVALUE, "Ambient"),
    (D3DCOLORVALUE, "Specular"),
    (D3DCOLORVALUE, "Emissive"),
    (Float, "Power"),
])

D3DLIGHTTYPE = Enum("D3DLIGHTTYPE", [
    "D3DLIGHT_POINT",
    "D3DLIGHT_SPOT",
    "D3DLIGHT_DIRECTIONAL",
])

D3DLIGHT9 = Struct("D3DLIGHT9", [
    (D3DLIGHTTYPE, "Type"),
    (D3DCOLORVALUE, "Diffuse"),
    (D3DCOLORVALUE, "Specular"),
    (D3DCOLORVALUE, "Ambient"),
    (D3DVECTOR, "Position"),
    (D3DVECTOR, "Direction"),
    (Float, "Range"),
    (Float, "Falloff"),
    (Float, "Attenuation0"),
    (Float, "Attenuation1"),
    (Float, "Attenuation2"),
    (Float, "Theta"),
    (Float, "Phi"),
])

D3DCLEAR = Flags(DWORD, [
    "D3DCLEAR_TARGET",
    "D3DCLEAR_ZBUFFER",
    "D3DCLEAR_STENCIL",
])

D3DSHADEMODE = Enum("D3DSHADEMODE", [
    "D3DSHADE_FLAT",
    "D3DSHADE_GOURAUD",
    "D3DSHADE_PHONG",
])

D3DFILLMODE = Enum("D3DFILLMODE", [
    "D3DFILL_POINT",
    "D3DFILL_WIREFRAME",
    "D3DFILL_SOLID",
])

D3DBLEND = Enum("D3DBLEND", [
    "D3DBLEND_ZERO",
    "D3DBLEND_ONE",
    "D3DBLEND_SRCCOLOR",
    "D3DBLEND_INVSRCCOLOR",
    "D3DBLEND_SRCALPHA",
    "D3DBLEND_INVSRCALPHA",
    "D3DBLEND_DESTALPHA",
    "D3DBLEND_INVDESTALPHA",
    "D3DBLEND_DESTCOLOR",
    "D3DBLEND_INVDESTCOLOR",
    "D3DBLEND_SRCALPHASAT",
    "D3DBLEND_BOTHSRCALPHA",
    "D3DBLEND_BOTHINVSRCALPHA",
    "D3DBLEND_BLENDFACTOR",
    "D3DBLEND_INVBLENDFACTOR",
    "D3DBLEND_SRCCOLOR2",
    "D3DBLEND_INVSRCCOLOR2",
])

D3DBLENDOP = Enum("D3DBLENDOP", [
    "D3DBLENDOP_ADD",
    "D3DBLENDOP_SUBTRACT",
    "D3DBLENDOP_REVSUBTRACT",
    "D3DBLENDOP_MIN",
    "D3DBLENDOP_MAX",
])

D3DTEXTUREADDRESS = Enum("D3DTEXTUREADDRESS", [
    "D3DTADDRESS_WRAP",
    "D3DTADDRESS_MIRROR",
    "D3DTADDRESS_CLAMP",
    "D3DTADDRESS_BORDER",
    "D3DTADDRESS_MIRRORONCE",
])

D3DCULL = Enum("D3DCULL", [
    "D3DCULL_NONE",
    "D3DCULL_CW",
    "D3DCULL_CCW",
])

D3DCMPFUNC = Enum("D3DCMPFUNC", [
    "D3DCMP_NEVER",
    "D3DCMP_LESS",
    "D3DCMP_EQUAL",
    "D3DCMP_LESSEQUAL",
    "D3DCMP_GREATER",
    "D3DCMP_NOTEQUAL",
    "D3DCMP_GREATEREQUAL",
    "D3DCMP_ALWAYS",
])

D3DSTENCILOP = Enum("D3DSTENCILOP", [
    "D3DSTENCILOP_KEEP",
    "D3DSTENCILOP_ZERO",
    "D3DSTENCILOP_REPLACE",
    "D3DSTENCILOP_INCRSAT",
    "D3DSTENCILOP_DECRSAT",
    "D3DSTENCILOP_INVERT",
    "D3DSTENCILOP_INCR",
    "D3DSTENCILOP_DECR",
])

D3DFOGMODE = Enum("D3DFOGMODE", [
    "D3DFOG_NONE",
    "D3DFOG_EXP",
    "D3DFOG_EXP2",
    "D3DFOG_LINEAR",
])

D3DZBUFFERTYPE = Enum("D3DZBUFFERTYPE", [
    "D3DZB_FALSE",
    "D3DZB_TRUE",
    "D3DZB_USEW",
])

D3DPRIMITIVETYPE = Enum("D3DPRIMITIVETYPE", [
    "D3DPT_POINTLIST",
    "D3DPT_LINELIST",
    "D3DPT_LINESTRIP",
    "D3DPT_TRIANGLELIST",
    "D3DPT_TRIANGLESTRIP",
    "D3DPT_TRIANGLEFAN",
])

D3DTRANSFORMSTATETYPE = Enum("D3DTRANSFORMSTATETYPE", [
    "D3DTS_VIEW",
    "D3DTS_PROJECTION",
    "D3DTS_TEXTURE0",
    "D3DTS_TEXTURE1",
    "D3DTS_TEXTURE2",
    "D3DTS_TEXTURE3",
    "D3DTS_TEXTURE4",
    "D3DTS_TEXTURE5",
    "D3DTS_TEXTURE6",
    "D3DTS_TEXTURE7",
])

D3DTS = Flags(DWORD, [
    "D3DTS_WORLD",
    "D3DTS_WORLD1",
    "D3DTS_WORLD2",
    "D3DTS_WORLD3",
])

D3DMATERIALCOLORSOURCE = Enum("D3DMATERIALCOLORSOURCE", [
    "D3DMCS_MATERIAL",
    "D3DMCS_COLOR1",
    "D3DMCS_COLOR2",
])

D3DWRAPCOORD = Flags(DWORD, [
    "D3DWRAPCOORD_0",
    "D3DWRAPCOORD_1",
    "D3DWRAPCOORD_2",
    "D3DWRAPCOORD_3",
])

D3DCOLORWRITEENABLE = Flags(DWORD, [
    "D3DCOLORWRITEENABLE_RED",
    "D3DCOLORWRITEENABLE_GREEN",
    "D3DCOLORWRITEENABLE_BLUE",
    "D3DCOLORWRITEENABLE_ALPHA",
])

D3DDEGREETYPE = Enum("D3DDEGREETYPE", [
    "D3DDEGREE_LINEAR",
    "D3DDEGREE_QUADRATIC",
    "D3DDEGREE_CUBIC",
    "D3DDEGREE_QUINTIC",
])

D3DPATCHEDGESTYLE = Enum("D3DPATCHEDGESTYLE", [
    "D3DPATCHEDGE_DISCRETE",
    "D3DPATCHEDGE_CONTINUOUS",
])

D3DVERTEXBLENDFLAGS = Enum("D3DVERTEXBLENDFLAGS", [
    "D3DVBF_DISABLE",
    "D3DVBF_1WEIGHTS",
    "D3DVBF_2WEIGHTS",
    "D3DVBF_3WEIGHTS",
    "D3DVBF_TWEENING",
    "D3DVBF_0WEIGHTS",
])

D3DDEBUGMONITORTOKENS = Enum("D3DDEBUGMONITORTOKENS", [
    "D3DDMT_ENABLE",
    "D3DDMT_DISABLE",
])

# TODO: Convert these to/from actual floats
FLOAT_AS_DWORD = DWORD

D3DRENDERSTATETYPE, D3DRENDERSTATEVALUE = EnumPolymorphic("D3DRENDERSTATETYPE", "State", [
    ("D3DRS_ZENABLE", D3DZBUFFERTYPE),
    ("D3DRS_FILLMODE", D3DFILLMODE),
    ("D3DRS_SHADEMODE", D3DSHADEMODE),
    ("D3DRS_ZWRITEENABLE", BOOL),
    ("D3DRS_ALPHATESTENABLE", BOOL),
    ("D3DRS_LASTPIXEL", BOOL),
    ("D3DRS_SRCBLEND", D3DBLEND),
    ("D3DRS_DESTBLEND", D3DBLEND),
    ("D3DRS_CULLMODE", D3DCULL),
    ("D3DRS_ZFUNC", D3DCMPFUNC),
    ("D3DRS_ALPHAREF", DWORD),
    ("D3DRS_ALPHAFUNC", D3DCMPFUNC),
    ("D3DRS_DITHERENABLE", BOOL),
    ("D3DRS_ALPHABLENDENABLE", BOOL),
    ("D3DRS_FOGENABLE", BOOL),
    ("D3DRS_SPECULARENABLE", BOOL),
    ("D3DRS_FOGCOLOR", D3DCOLOR),
    ("D3DRS_FOGTABLEMODE", D3DFOGMODE),
    ("D3DRS_FOGSTART", FLOAT_AS_DWORD),
    ("D3DRS_FOGEND", FLOAT_AS_DWORD),
    ("D3DRS_FOGDENSITY", FLOAT_AS_DWORD),
    ("D3DRS_RANGEFOGENABLE", BOOL),
    ("D3DRS_STENCILENABLE", BOOL),
    ("D3DRS_STENCILFAIL", D3DSTENCILOP),
    ("D3DRS_STENCILZFAIL", D3DSTENCILOP),
    ("D3DRS_STENCILPASS", D3DSTENCILOP),
    ("D3DRS_STENCILFUNC", D3DCMPFUNC),
    ("D3DRS_STENCILREF", DWORD),
    ("D3DRS_STENCILMASK", DWORD),
    ("D3DRS_STENCILWRITEMASK", DWORD),
    ("D3DRS_TEXTUREFACTOR", D3DCOLOR),
    ("D3DRS_WRAP0", D3DWRAPCOORD),
    ("D3DRS_WRAP1", D3DWRAPCOORD),
    ("D3DRS_WRAP2", D3DWRAPCOORD),
    ("D3DRS_WRAP3", D3DWRAPCOORD),
    ("D3DRS_WRAP4", D3DWRAPCOORD),
    ("D3DRS_WRAP5", D3DWRAPCOORD),
    ("D3DRS_WRAP6", D3DWRAPCOORD),
    ("D3DRS_WRAP7", D3DWRAPCOORD),
    ("D3DRS_CLIPPING", BOOL),
    ("D3DRS_LIGHTING", BOOL),
    ("D3DRS_AMBIENT", D3DCOLOR),
    ("D3DRS_FOGVERTEXMODE", D3DFOGMODE),
    ("D3DRS_COLORVERTEX", BOOL),
    ("D3DRS_LOCALVIEWER", BOOL),
    ("D3DRS_NORMALIZENORMALS", BOOL),
    ("D3DRS_DIFFUSEMATERIALSOURCE", D3DMATERIALCOLORSOURCE),
    ("D3DRS_SPECULARMATERIALSOURCE", D3DMATERIALCOLORSOURCE),
    ("D3DRS_AMBIENTMATERIALSOURCE", D3DMATERIALCOLORSOURCE),
    ("D3DRS_EMISSIVEMATERIALSOURCE", D3DMATERIALCOLORSOURCE),
    ("D3DRS_VERTEXBLEND", D3DVERTEXBLENDFLAGS),
    ("D3DRS_CLIPPLANEENABLE", D3DCLIPPLANE),
    ("D3DRS_POINTSIZE", FLOAT_AS_DWORD),
    ("D3DRS_POINTSIZE_MIN", FLOAT_AS_DWORD),
    ("D3DRS_POINTSPRITEENABLE", BOOL),
    ("D3DRS_POINTSCALEENABLE", BOOL),
    ("D3DRS_POINTSCALE_A", FLOAT_AS_DWORD),
    ("D3DRS_POINTSCALE_B", FLOAT_AS_DWORD),
    ("D3DRS_POINTSCALE_C", FLOAT_AS_DWORD),
    ("D3DRS_MULTISAMPLEANTIALIAS", BOOL),
    ("D3DRS_MULTISAMPLEMASK", DWORD),
    ("D3DRS_PATCHEDGESTYLE", D3DPATCHEDGESTYLE),
    ("D3DRS_DEBUGMONITORTOKEN", D3DDEBUGMONITORTOKENS),
    ("D3DRS_POINTSIZE_MAX", FLOAT_AS_DWORD),
    ("D3DRS_INDEXEDVERTEXBLENDENABLE", BOOL),
    ("D3DRS_COLORWRITEENABLE", DWORD),
    ("D3DRS_TWEENFACTOR", FLOAT_AS_DWORD),
    ("D3DRS_BLENDOP", D3DBLENDOP),
    ("D3DRS_POSITIONDEGREE", D3DDEGREETYPE),
    ("D3DRS_NORMALDEGREE", D3DDEGREETYPE),
    ("D3DRS_SCISSORTESTENABLE", BOOL),
    ("D3DRS_SLOPESCALEDEPTHBIAS", FLOAT_AS_DWORD),
    ("D3DRS_ANTIALIASEDLINEENABLE", BOOL),
    ("D3DRS_MINTESSELLATIONLEVEL", FLOAT_AS_DWORD),
    ("D3DRS_MAXTESSELLATIONLEVEL", FLOAT_AS_DWORD),
    ("D3DRS_ADAPTIVETESS_X", FLOAT_AS_DWORD),
    ("D3DRS_ADAPTIVETESS_Y", FLOAT_AS_DWORD),
    ("D3DRS_ADAPTIVETESS_Z", FLOAT_AS_DWORD),
    ("D3DRS_ADAPTIVETESS_W", FLOAT_AS_DWORD),
    ("D3DRS_ENABLEADAPTIVETESSELLATION", BOOL),
    ("D3DRS_TWOSIDEDSTENCILMODE", BOOL),
    ("D3DRS_CCW_STENCILFAIL", D3DSTENCILOP),
    ("D3DRS_CCW_STENCILZFAIL", D3DSTENCILOP),
    ("D3DRS_CCW_STENCILPASS", D3DSTENCILOP),
    ("D3DRS_CCW_STENCILFUNC", D3DCMPFUNC),
    ("D3DRS_COLORWRITEENABLE1", D3DCOLORWRITEENABLE),
    ("D3DRS_COLORWRITEENABLE2", D3DCOLORWRITEENABLE),
    ("D3DRS_COLORWRITEENABLE3", D3DCOLORWRITEENABLE),
    ("D3DRS_BLENDFACTOR", D3DCOLOR),
    ("D3DRS_SRGBWRITEENABLE", BOOL),
    ("D3DRS_DEPTHBIAS", FLOAT_AS_DWORD),
    ("D3DRS_WRAP8", D3DWRAPCOORD),
    ("D3DRS_WRAP9", D3DWRAPCOORD),
    ("D3DRS_WRAP10", D3DWRAPCOORD),
    ("D3DRS_WRAP11", D3DWRAPCOORD),
    ("D3DRS_WRAP12", D3DWRAPCOORD),
    ("D3DRS_WRAP13", D3DWRAPCOORD),
    ("D3DRS_WRAP14", D3DWRAPCOORD),
    ("D3DRS_WRAP15", D3DWRAPCOORD),
    ("D3DRS_SEPARATEALPHABLENDENABLE", BOOL),
    ("D3DRS_SRCBLENDALPHA", D3DBLEND),
    ("D3DRS_DESTBLENDALPHA", D3DBLEND),
    ("D3DRS_BLENDOPALPHA", D3DBLENDOP),

    # XXX: D3DRENDERSTATE_WRAPBIAS + n
], DWORD)

D3DTSS_TCI = Flags(DWORD, [
    #"D3DTSS_TCI_PASSTHRU", # 0
    "D3DTSS_TCI_CAMERASPACENORMAL",
    "D3DTSS_TCI_CAMERASPACEPOSITION",
    "D3DTSS_TCI_CAMERASPACEREFLECTIONVECTOR",
    "D3DTSS_TCI_SPHEREMAP",
])

D3DTEXTUREOP = Enum("D3DTEXTUREOP", [
    "D3DTOP_DISABLE",
    "D3DTOP_SELECTARG1",
    "D3DTOP_SELECTARG2",
    "D3DTOP_MODULATE",
    "D3DTOP_MODULATE2X",
    "D3DTOP_MODULATE4X",
    "D3DTOP_ADD",
    "D3DTOP_ADDSIGNED",
    "D3DTOP_ADDSIGNED2X",
    "D3DTOP_SUBTRACT",
    "D3DTOP_ADDSMOOTH",
    "D3DTOP_BLENDDIFFUSEALPHA",
    "D3DTOP_BLENDTEXTUREALPHA",
    "D3DTOP_BLENDFACTORALPHA",
    "D3DTOP_BLENDTEXTUREALPHAPM",
    "D3DTOP_BLENDCURRENTALPHA",
    "D3DTOP_PREMODULATE",
    "D3DTOP_MODULATEALPHA_ADDCOLOR",
    "D3DTOP_MODULATECOLOR_ADDALPHA",
    "D3DTOP_MODULATEINVALPHA_ADDCOLOR",
    "D3DTOP_MODULATEINVCOLOR_ADDALPHA",
    "D3DTOP_BUMPENVMAP",
    "D3DTOP_BUMPENVMAPLUMINANCE",
    "D3DTOP_DOTPRODUCT3",
    "D3DTOP_MULTIPLYADD",
    "D3DTOP_LERP",
])

# XXX: Actually a mixture of enums and flags
D3DTA = FakeEnum(DWORD, [
    "D3DTA_DIFFUSE",
    "D3DTA_CURRENT",
    "D3DTA_TEXTURE",
    "D3DTA_TFACTOR",
    "D3DTA_SPECULAR",
    "D3DTA_TEMP",
    "D3DTA_CONSTANT",
    #"D3DTA_COMPLEMENT",
    #"D3DTA_ALPHAREPLICATE",
])

D3DTEXTURETRANSFORMFLAGS = Enum("D3DTEXTURETRANSFORMFLAGS", [
    "D3DTTFF_DISABLE",
    "D3DTTFF_COUNT1",
    "D3DTTFF_COUNT2",
    "D3DTTFF_COUNT3",
    "D3DTTFF_COUNT4",
    "D3DTTFF_PROJECTED",
])

D3DTEXTUREFILTERTYPE = Enum("D3DTEXTUREFILTERTYPE", [
    "D3DTEXF_NONE",
    "D3DTEXF_POINT",
    "D3DTEXF_LINEAR",
    "D3DTEXF_ANISOTROPIC",
    "D3DTEXF_PYRAMIDALQUAD",
    "D3DTEXF_GAUSSIANQUAD",
    "D3DTEXF_CONVOLUTIONMONO",
])

D3DTEXTURESTAGESTATETYPE, D3DTEXTURESTAGESTATEVALUE = EnumPolymorphic("D3DTEXTURESTAGESTATETYPE", "Type", [
    ("D3DTSS_COLOROP", D3DTEXTUREOP),
    ("D3DTSS_COLORARG1", D3DTA),
    ("D3DTSS_COLORARG2", D3DTA),
    ("D3DTSS_ALPHAOP", D3DTEXTUREOP),
    ("D3DTSS_ALPHAARG1", D3DTA),
    ("D3DTSS_ALPHAARG2", D3DTA),
    ("D3DTSS_BUMPENVMAT00", FLOAT_AS_DWORD),
    ("D3DTSS_BUMPENVMAT01", FLOAT_AS_DWORD),
    ("D3DTSS_BUMPENVMAT10", FLOAT_AS_DWORD),
    ("D3DTSS_BUMPENVMAT11", FLOAT_AS_DWORD),
    ("D3DTSS_TEXCOORDINDEX", D3DTSS_TCI),
    ("D3DTSS_BUMPENVLSCALE", FLOAT_AS_DWORD),
    ("D3DTSS_BUMPENVLOFFSET", FLOAT_AS_DWORD),
    ("D3DTSS_TEXTURETRANSFORMFLAGS", D3DTEXTURETRANSFORMFLAGS),
    ("D3DTSS_COLORARG0", D3DTA,),
    ("D3DTSS_ALPHAARG0", D3DTA,),
    ("D3DTSS_RESULTARG", D3DTA,),
    ("D3DTSS_CONSTANT", D3DCOLOR),
], DWORD)

D3DSAMPLERSTATETYPE, D3DSAMPLERSTATEVALUE = EnumPolymorphic("D3DSAMPLERSTATETYPE", "Type", [
    ("D3DSAMP_ADDRESSU", D3DTEXTUREADDRESS),
    ("D3DSAMP_ADDRESSV", D3DTEXTUREADDRESS),
    ("D3DSAMP_ADDRESSW", D3DTEXTUREADDRESS),
    ("D3DSAMP_BORDERCOLOR", D3DCOLOR),
    ("D3DSAMP_MAGFILTER", D3DTEXTUREFILTERTYPE),
    ("D3DSAMP_MINFILTER", D3DTEXTUREFILTERTYPE),
    ("D3DSAMP_MIPFILTER", D3DTEXTUREFILTERTYPE),
    ("D3DSAMP_MIPMAPLODBIAS", FLOAT_AS_DWORD),
    ("D3DSAMP_MAXMIPLEVEL", DWORD),
    ("D3DSAMP_MAXANISOTROPY", DWORD),
    ("D3DSAMP_SRGBTEXTURE", BOOL),
    ("D3DSAMP_ELEMENTINDEX", DWORD),
    ("D3DSAMP_DMAPOFFSET", DWORD),
], DWORD)

D3DPV = Flags(DWORD, [
    "D3DPV_DONOTCOPYDATA",
])

# XXX: Actually a mixture of enums and flags
D3DFVF = Flags(DWORD, [
    "D3DFVF_RESERVED0",
    "D3DFVF_XYZ",
    "D3DFVF_XYZRHW",
    "D3DFVF_XYZB1",
    "D3DFVF_XYZB2",
    "D3DFVF_XYZB3",
    "D3DFVF_XYZB4",
    "D3DFVF_XYZB5",
    "D3DFVF_XYZW",
    "D3DFVF_NORMAL",
    "D3DFVF_PSIZE",
    "D3DFVF_DIFFUSE",
    "D3DFVF_SPECULAR",
    #"D3DFVF_TEX0",
    #"D3DFVF_TEX1",
    #"D3DFVF_TEX2",
    #"D3DFVF_TEX3",
    #"D3DFVF_TEX4",
    #"D3DFVF_TEX5",
    #"D3DFVF_TEX6",
    #"D3DFVF_TEX7",
    #"D3DFVF_TEX8",
    "D3DFVF_LASTBETA_UBYTE4",
    "D3DFVF_LASTBETA_D3DCOLOR",
    "D3DFVF_RESERVED2",
    #"D3DFVF_TEXCOORDSIZE1(0)",
    #"D3DFVF_TEXCOORDSIZE2(0)",
    #"D3DFVF_TEXCOORDSIZE3(0)",
    #"D3DFVF_TEXCOORDSIZE4(0)",
    #"D3DFVF_TEXCOORDSIZE1(1)",
    #"D3DFVF_TEXCOORDSIZE2(1)",
    #"D3DFVF_TEXCOORDSIZE3(1)",
    #"D3DFVF_TEXCOORDSIZE4(1)",
    #"D3DFVF_TEXCOORDSIZE1(2)",
    #"D3DFVF_TEXCOORDSIZE2(2)",
    #"D3DFVF_TEXCOORDSIZE3(2)",
    #"D3DFVF_TEXCOORDSIZE4(2)",
    #"D3DFVF_TEXCOORDSIZE1(3)",
    #"D3DFVF_TEXCOORDSIZE2(3)",
    #"D3DFVF_TEXCOORDSIZE3(3)",
    #"D3DFVF_TEXCOORDSIZE4(3)",
])

D3DDECLUSAGE = FakeEnum(BYTE, [
    "D3DDECLUSAGE_POSITION",
    "D3DDECLUSAGE_BLENDWEIGHT",
    "D3DDECLUSAGE_BLENDINDICES",
    "D3DDECLUSAGE_NORMAL",
    "D3DDECLUSAGE_PSIZE",
    "D3DDECLUSAGE_TEXCOORD",
    "D3DDECLUSAGE_TANGENT",
    "D3DDECLUSAGE_BINORMAL",
    "D3DDECLUSAGE_TESSFACTOR",
    "D3DDECLUSAGE_POSITIONT",
    "D3DDECLUSAGE_COLOR",
    "D3DDECLUSAGE_FOG",
    "D3DDECLUSAGE_DEPTH",
    "D3DDECLUSAGE_SAMPLE",
])

D3DDECLMETHOD = FakeEnum(BYTE, [
    "D3DDECLMETHOD_DEFAULT",
    "D3DDECLMETHOD_PARTIALU",
    "D3DDECLMETHOD_PARTIALV",
    "D3DDECLMETHOD_CROSSUV",
    "D3DDECLMETHOD_UV",
    "D3DDECLMETHOD_LOOKUP",
    "D3DDECLMETHOD_LOOKUPPRESAMPLED",
])

D3DDECLTYPE = FakeEnum(BYTE, [
    "D3DDECLTYPE_FLOAT1",
    "D3DDECLTYPE_FLOAT2",
    "D3DDECLTYPE_FLOAT3",
    "D3DDECLTYPE_FLOAT4",
    "D3DDECLTYPE_D3DCOLOR",
    "D3DDECLTYPE_UBYTE4",
    "D3DDECLTYPE_SHORT2",
    "D3DDECLTYPE_SHORT4",
    "D3DDECLTYPE_UBYTE4N",
    "D3DDECLTYPE_SHORT2N",
    "D3DDECLTYPE_SHORT4N",
    "D3DDECLTYPE_USHORT2N",
    "D3DDECLTYPE_USHORT4N",
    "D3DDECLTYPE_UDEC3",
    "D3DDECLTYPE_DEC3N",
    "D3DDECLTYPE_FLOAT16_2",
    "D3DDECLTYPE_FLOAT16_4",
    "D3DDECLTYPE_UNUSED",
])

D3DVERTEXELEMENT9 = Struct("D3DVERTEXELEMENT9", [
    (WORD, "Stream"),
    (WORD, "Offset"),
    (D3DDECLTYPE, "Type"), # BYTE
    (D3DDECLMETHOD, "Method"), # BYTE
    (D3DDECLUSAGE, "Usage"), # BYTE
    (BYTE, "UsageIndex"),
])

D3DBASISTYPE = Enum("D3DBASISTYPE", [
    "D3DBASIS_BEZIER",
    "D3DBASIS_BSPLINE",
    "D3DBASIS_CATMULL_ROM",
])

D3DSTATEBLOCKTYPE = Enum("D3DSTATEBLOCKTYPE", [
    "D3DSBT_ALL",
    "D3DSBT_PIXELSTATE",
    "D3DSBT_VERTEXSTATE",
])

D3DDEVTYPE = Enum("D3DDEVTYPE", [
    "D3DDEVTYPE_HAL",
    "D3DDEVTYPE_REF",
    "D3DDEVTYPE_SW",
    "D3DDEVTYPE_NULLREF",
])

D3DMULTISAMPLE_TYPE = Enum("D3DMULTISAMPLE_TYPE", [
    "D3DMULTISAMPLE_NONE",
    "D3DMULTISAMPLE_NONMASKABLE",
    "D3DMULTISAMPLE_2_SAMPLES",
    "D3DMULTISAMPLE_3_SAMPLES",
    "D3DMULTISAMPLE_4_SAMPLES",
    "D3DMULTISAMPLE_5_SAMPLES",
    "D3DMULTISAMPLE_6_SAMPLES",
    "D3DMULTISAMPLE_7_SAMPLES",
    "D3DMULTISAMPLE_8_SAMPLES",
    "D3DMULTISAMPLE_9_SAMPLES",
    "D3DMULTISAMPLE_10_SAMPLES",
    "D3DMULTISAMPLE_11_SAMPLES",
    "D3DMULTISAMPLE_12_SAMPLES",
    "D3DMULTISAMPLE_13_SAMPLES",
    "D3DMULTISAMPLE_14_SAMPLES",
    "D3DMULTISAMPLE_15_SAMPLES",
    "D3DMULTISAMPLE_16_SAMPLES",
])

D3DFORMAT = Enum("D3DFORMAT", [
    "D3DFMT_UNKNOWN",
    "D3DFMT_R8G8B8",
    "D3DFMT_A8R8G8B8",
    "D3DFMT_X8R8G8B8",
    "D3DFMT_R5G6B5",
    "D3DFMT_X1R5G5B5",
    "D3DFMT_A1R5G5B5",
    "D3DFMT_A4R4G4B4",
    "D3DFMT_R3G3B2",
    "D3DFMT_A8",
    "D3DFMT_A8R3G3B2",
    "D3DFMT_X4R4G4B4",
    "D3DFMT_A2B10G10R10",
    "D3DFMT_A8B8G8R8",
    "D3DFMT_X8B8G8R8",
    "D3DFMT_G16R16",
    "D3DFMT_A2R10G10B10",
    "D3DFMT_A16B16G16R16",
    "D3DFMT_A8P8",
    "D3DFMT_P8",
    "D3DFMT_L8",
    "D3DFMT_A8L8",
    "D3DFMT_A4L4",
    "D3DFMT_V8U8",
    "D3DFMT_L6V5U5",
    "D3DFMT_X8L8V8U8",
    "D3DFMT_Q8W8V8U8",
    "D3DFMT_V16U16",
    "D3DFMT_A2W10V10U10",
    "D3DFMT_UYVY",
    "D3DFMT_R8G8_B8G8",
    "D3DFMT_YUY2",
    "D3DFMT_G8R8_G8B8",
    "D3DFMT_DXT1",
    "D3DFMT_DXT2",
    "D3DFMT_DXT3",
    "D3DFMT_DXT4",
    "D3DFMT_DXT5",
    "D3DFMT_D16_LOCKABLE",
    "D3DFMT_D32",
    "D3DFMT_D15S1",
    "D3DFMT_D24S8",
    "D3DFMT_D24X8",
    "D3DFMT_D24X4S4",
    "D3DFMT_D16",
    "D3DFMT_D32F_LOCKABLE",
    "D3DFMT_D24FS8",
    "D3DFMT_D32_LOCKABLE",
    "D3DFMT_S8_LOCKABLE",
    "D3DFMT_L16",
    "D3DFMT_VERTEXDATA",
    "D3DFMT_INDEX16",
    "D3DFMT_INDEX32",
    "D3DFMT_Q16W16V16U16",
    "D3DFMT_MULTI2_ARGB8",
    "D3DFMT_R16F",
    "D3DFMT_G16R16F",
    "D3DFMT_A16B16G16R16F",
    "D3DFMT_R32F",
    "D3DFMT_G32R32F",
    "D3DFMT_A32B32G32R32F",
    "D3DFMT_CxV8U8",
    "D3DFMT_A1",
    "D3DFMT_A2B10G10R10_XR_BIAS",
    "D3DFMT_BINARYBUFFER",

    # Unofficial formats
    "D3DFMT_ATI1N",
    "D3DFMT_ATI2N",
    "D3DFMT_AYUV",
    "D3DFMT_DF16",
    "D3DFMT_DF24",
    "D3DFMT_INTZ",
    "D3DFMT_NULL",
    "D3DFMT_NV12",
    "D3DFMT_RAWZ",
])

D3DDISPLAYMODE = Struct("D3DDISPLAYMODE", [
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "RefreshRate"),
    (D3DFORMAT, "Format"),
])

D3DCREATE = Flags(DWORD, [
    "D3DCREATE_FPU_PRESERVE",
    "D3DCREATE_MULTITHREADED",
    "D3DCREATE_PUREDEVICE",
    "D3DCREATE_SOFTWARE_VERTEXPROCESSING",
    "D3DCREATE_HARDWARE_VERTEXPROCESSING",
    "D3DCREATE_MIXED_VERTEXPROCESSING",
    "D3DCREATE_DISABLE_DRIVER_MANAGEMENT",
    "D3DCREATE_ADAPTERGROUP_DEVICE",
    "D3DCREATE_DISABLE_DRIVER_MANAGEMENT_EX",
    "D3DCREATE_NOWINDOWCHANGES",
    "D3DCREATE_DISABLE_PSGP_THREADING",
    "D3DCREATE_ENABLE_PRESENTSTATS",
    "D3DCREATE_DISABLE_PRINTSCREEN",
    "D3DCREATE_SCREENSAVER",
])

D3DDEVICE_CREATION_PARAMETERS = Struct("D3DDEVICE_CREATION_PARAMETERS", [
    (UINT, "AdapterOrdinal"),
    (D3DDEVTYPE, "DeviceType"),
    (HWND, "hFocusWindow"),
    (D3DCREATE, "BehaviorFlags"),
])

D3DSWAPEFFECT = Enum("D3DSWAPEFFECT", [
    "D3DSWAPEFFECT_DISCARD",
    "D3DSWAPEFFECT_FLIP",
    "D3DSWAPEFFECT_COPY",
])

D3DPOOL = Enum("D3DPOOL", [
    "D3DPOOL_DEFAULT",
    "D3DPOOL_MANAGED",
    "D3DPOOL_SYSTEMMEM",
    "D3DPOOL_SCRATCH",
])

D3DPRESENT = FakeEnum(DWORD, [
    "D3DPRESENT_RATE_DEFAULT",
])

D3DPRESENTFLAG = Flags(DWORD, [
    "D3DPRESENTFLAG_LOCKABLE_BACKBUFFER",
    "D3DPRESENTFLAG_DISCARD_DEPTHSTENCIL",
    "D3DPRESENTFLAG_DEVICECLIP",
    "D3DPRESENTFLAG_VIDEO",
    "D3DPRESENTFLAG_NOAUTOROTATE",
    "D3DPRESENTFLAG_UNPRUNEDMODE",
])

D3DPRESENT_INTERVAL = Flags(DWORD, [
    "D3DPRESENT_INTERVAL_DEFAULT", # 0
    "D3DPRESENT_INTERVAL_ONE",
    "D3DPRESENT_INTERVAL_TWO",
    "D3DPRESENT_INTERVAL_THREE",
    "D3DPRESENT_INTERVAL_FOUR",
    "D3DPRESENT_INTERVAL_IMMEDIATE",
])

D3DPRESENT_PARAMETERS = Struct("D3DPRESENT_PARAMETERS", [
    (UINT, "BackBufferWidth"),
    (UINT, "BackBufferHeight"),
    (D3DFORMAT, "BackBufferFormat"),
    (UINT, "BackBufferCount"),
    (D3DMULTISAMPLE_TYPE, "MultiSampleType"),
    (DWORD, "MultiSampleQuality"),
    (D3DSWAPEFFECT, "SwapEffect"),
    (HWND, "hDeviceWindow"),
    (BOOL, "Windowed"),
    (BOOL, "EnableAutoDepthStencil"),
    (D3DFORMAT, "AutoDepthStencilFormat"),
    (D3DPRESENTFLAG, "Flags"),
    (UINT, "FullScreen_RefreshRateInHz"),
    (D3DPRESENT_INTERVAL, "PresentationInterval"),
])

D3DGAMMARAMP = Struct("D3DGAMMARAMP", [
    (Array(WORD, 256), "red"),
    (Array(WORD, 256), "green"),
    (Array(WORD, 256), "blue"),
])

D3DBACKBUFFER_TYPE = Enum("D3DBACKBUFFER_TYPE", [
    "D3DBACKBUFFER_TYPE_MONO",
    "D3DBACKBUFFER_TYPE_LEFT",
    "D3DBACKBUFFER_TYPE_RIGHT",
])

D3DRESOURCETYPE = Enum("D3DRESOURCETYPE", [
    "D3DRTYPE_SURFACE",
    "D3DRTYPE_VOLUME",
    "D3DRTYPE_TEXTURE",
    "D3DRTYPE_VOLUMETEXTURE",
    "D3DRTYPE_CUBETEXTURE",
    "D3DRTYPE_VERTEXBUFFER",
    "D3DRTYPE_INDEXBUFFER",
])

D3DUSAGE = Flags(DWORD, [
    "D3DUSAGE_RENDERTARGET",
    "D3DUSAGE_DEPTHSTENCIL",
    "D3DUSAGE_WRITEONLY",
    "D3DUSAGE_SOFTWAREPROCESSING",
    "D3DUSAGE_DONOTCLIP",
    "D3DUSAGE_POINTS",
    "D3DUSAGE_RTPATCHES",
    "D3DUSAGE_NPATCHES",
    "D3DUSAGE_DYNAMIC",
    "D3DUSAGE_AUTOGENMIPMAP",
    "D3DUSAGE_RESTRICTED_CONTENT",
    "D3DUSAGE_RESTRICT_SHARED_RESOURCE",
    "D3DUSAGE_RESTRICT_SHARED_RESOURCE_DRIVER",
    "D3DUSAGE_DMAP",
    "D3DUSAGE_QUERY_LEGACYBUMPMAP",
    "D3DUSAGE_QUERY_SRGBREAD",
    "D3DUSAGE_QUERY_FILTER",
    "D3DUSAGE_QUERY_SRGBWRITE",
    "D3DUSAGE_QUERY_POSTPIXELSHADER_BLENDING",
    "D3DUSAGE_QUERY_VERTEXTEXTURE",
    "D3DUSAGE_QUERY_WRAPANDMIP",
    "D3DUSAGE_NONSECURE",
    "D3DUSAGE_TEXTAPI",
])

D3DCUBEMAP_FACES = Enum("D3DCUBEMAP_FACES", [
    "D3DCUBEMAP_FACE_POSITIVE_X",
    "D3DCUBEMAP_FACE_NEGATIVE_X",
    "D3DCUBEMAP_FACE_POSITIVE_Y",
    "D3DCUBEMAP_FACE_NEGATIVE_Y",
    "D3DCUBEMAP_FACE_POSITIVE_Z",
    "D3DCUBEMAP_FACE_NEGATIVE_Z",
])

D3DLOCK = Flags(DWORD, [
    "D3DLOCK_READONLY",
    "D3DLOCK_DISCARD",
    "D3DLOCK_NOOVERWRITE",
    "D3DLOCK_NOSYSLOCK",
    "D3DLOCK_DONOTWAIT",
    "D3DLOCK_NO_DIRTY_UPDATE",
])

D3DVERTEXBUFFER_DESC = Struct("D3DVERTEXBUFFER_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (D3DUSAGE, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
    (DWORD, "FVF"),
])

D3DINDEXBUFFER_DESC = Struct("D3DINDEXBUFFER_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (D3DUSAGE, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
])

D3DSURFACE_DESC = Struct("D3DSURFACE_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (D3DUSAGE, "Usage"),
    (D3DPOOL, "Pool"),
    (D3DMULTISAMPLE_TYPE, "MultiSampleType"),
    (DWORD, "MultiSampleQuality"),
    (UINT, "Width"),
    (UINT, "Height"),
])

D3DVOLUME_DESC = Struct("D3DVOLUME_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (D3DUSAGE, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "Depth"),
])

D3DLOCKED_RECT = Struct("D3DLOCKED_RECT", [
    (INT, "Pitch"),
    (LinearPointer(Void, "_MappedSize"), "pBits"),
])

D3DBOX = Struct("D3DBOX", [
    (UINT, "Left"),
    (UINT, "Top"),
    (UINT, "Right"),
    (UINT, "Bottom"),
    (UINT, "Front"),
    (UINT, "Back"),
])

D3DLOCKED_BOX = Struct("D3DLOCKED_BOX", [
    (INT, "RowPitch"),
    (INT, "SlicePitch"),
    (LinearPointer(Void, "_MappedSize"), "pBits"),
])

D3DRANGE = Struct("D3DRANGE", [
    (UINT, "Offset"),
    (UINT, "Size"),
])

D3DRECTPATCH_INFO = Struct("D3DRECTPATCH_INFO", [
    (UINT, "StartVertexOffsetWidth"),
    (UINT, "StartVertexOffsetHeight"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "Stride"),
    (D3DBASISTYPE, "Basis"),
    (D3DDEGREETYPE, "Degree"),
])

D3DTRIPATCH_INFO = Struct("D3DTRIPATCH_INFO", [
    (UINT, "StartVertexOffset"),
    (UINT, "NumVertices"),
    (D3DBASISTYPE, "Basis"),
    (D3DDEGREETYPE, "Degree"),
])

D3DADAPTER_IDENTIFIER9 = Struct("D3DADAPTER_IDENTIFIER9", [
    (CString, "Driver"),
    (CString, "Description"),
    (CString, "DeviceName"),
    (LARGE_INTEGER, "DriverVersion"),
    (DWORD, "VendorId"),
    (DWORD, "DeviceId"),
    (DWORD, "SubSysId"),
    (DWORD, "Revision"),
    (GUID, "DeviceIdentifier"),
    (DWORD, "WHQLLevel"),
])

D3DRASTER_STATUS = Struct("D3DRASTER_STATUS", [
    (BOOL, "InVBlank"),
    (UINT, "ScanLine"),
])

D3DQUERYTYPE = Enum("D3DQUERYTYPE", [
    "D3DQUERYTYPE_VCACHE",
    "D3DQUERYTYPE_RESOURCEMANAGER",
    "D3DQUERYTYPE_VERTEXSTATS",
    "D3DQUERYTYPE_EVENT",
    "D3DQUERYTYPE_OCCLUSION",
    "D3DQUERYTYPE_TIMESTAMP",
    "D3DQUERYTYPE_TIMESTAMPDISJOINT",
    "D3DQUERYTYPE_TIMESTAMPFREQ",
    "D3DQUERYTYPE_PIPELINETIMINGS",
    "D3DQUERYTYPE_INTERFACETIMINGS",
    "D3DQUERYTYPE_VERTEXTIMINGS",
    "D3DQUERYTYPE_PIXELTIMINGS",
    "D3DQUERYTYPE_BANDWIDTHTIMINGS",
    "D3DQUERYTYPE_CACHEUTILIZATION",
])

D3DISSUE = Flags(DWORD, [
    "D3DISSUE_END",
    "D3DISSUE_BEGIN",
])

D3DGETDATA = Flags(DWORD, [
    "D3DGETDATA_FLUSH",
])

D3DRESOURCESTATS = Struct("D3DRESOURCESTATS", [
    (BOOL, "bThrashing"),
    (DWORD, "ApproxBytesDownloaded"),
    (DWORD, "NumEvicts"),
    (DWORD, "NumVidCreates"),
    (DWORD, "LastPri"),
    (DWORD, "NumUsed"),
    (DWORD, "NumUsedInVidMem"),
    (DWORD, "WorkingSet"),
    (DWORD, "WorkingSetBytes"),
    (DWORD, "TotalManaged"),
    (DWORD, "TotalBytes"),
])

D3DDEVINFO_RESOURCEMANAGER = Struct("D3DDEVINFO_RESOURCEMANAGER", [
    (Array(D3DRESOURCESTATS, "D3DRTYPECOUNT"), "stats"),
])

D3DDEVINFO_D3DVERTEXSTATS = Struct("D3DDEVINFO_D3DVERTEXSTATS", [
    (DWORD, "NumRenderedTriangles"),
    (DWORD, "NumExtraClippingTriangles"),
])

D3DDEVINFO_VCACHE = Struct("D3DDEVINFO_VCACHE", [
    (DWORD, "Pattern"),
    (DWORD, "OptMethod"),
    (DWORD, "CacheSize"),
    (DWORD, "MagicNumber"),
])

D3DDEVINFO_D3D9PIPELINETIMINGS = Struct("D3DDEVINFO_D3D9PIPELINETIMINGS", [
    (FLOAT, "VertexProcessingTimePercent"),
    (FLOAT, "PixelProcessingTimePercent"),
    (FLOAT, "OtherGPUProcessingTimePercent"),
    (FLOAT, "GPUIdleTimePercent"),
])

D3DDEVINFO_D3D9INTERFACETIMINGS = Struct("D3DDEVINFO_D3D9INTERFACETIMINGS", [
    (FLOAT, "WaitingForGPUToUseApplicationResourceTimePercent"),
    (FLOAT, "WaitingForGPUToAcceptMoreCommandsTimePercent"),
    (FLOAT, "WaitingForGPUToStayWithinLatencyTimePercent"),
    (FLOAT, "WaitingForGPUExclusiveResourceTimePercent"),
    (FLOAT, "WaitingForGPUOtherTimePercent"),
])

D3DDEVINFO_D3D9STAGETIMINGS = Struct("D3DDEVINFO_D3D9STAGETIMINGS", [
    (FLOAT, "MemoryProcessingPercent"),
    (FLOAT, "ComputationProcessingPercent"),
])

D3DDEVINFO_D3D9BANDWIDTHTIMINGS = Struct("D3DDEVINFO_D3D9BANDWIDTHTIMINGS", [
    (FLOAT, "MaxBandwidthUtilized"),
    (FLOAT, "FrontEndUploadMemoryUtilizedPercent"),
    (FLOAT, "VertexRateUtilizedPercent"),
    (FLOAT, "TriangleSetupRateUtilizedPercent"),
    (FLOAT, "FillRateUtilizedPercent"),
])

D3DDEVINFO_D3D9CACHEUTILIZATION = Struct("D3DDEVINFO_D3D9CACHEUTILIZATION", [
    (FLOAT, "TextureCacheHitRate"),
    (FLOAT, "PostTransformVertexCacheHitRate"),
])

D3DCOMPOSERECTSOP = Enum("D3DCOMPOSERECTSOP", [
    "D3DCOMPOSERECTS_COPY",
    "D3DCOMPOSERECTS_OR",
    "D3DCOMPOSERECTS_AND",
    "D3DCOMPOSERECTS_NEG",
])

D3DCOMPOSERECTDESC = Struct("D3DCOMPOSERECTDESC", [
    (USHORT, "X"),
    (USHORT, "Y"),
    (USHORT, "Width"),
    (USHORT, "Height"),
])

D3DCOMPOSERECTDESTINATION = Struct("D3DCOMPOSERECTDESTINATION", [
    (USHORT, "SrcRectIndex"),
    (USHORT, "Reserved"),
    (Short, "X"),
    (Short, "Y"),
])

D3DPRESENTSTATS = Struct("D3DPRESENTSTATS", [
    (UINT, "PresentCount"),
    (UINT, "PresentRefreshCount"),
    (UINT, "SyncRefreshCount"),
    (LARGE_INTEGER, "SyncQPCTime"),
    (LARGE_INTEGER, "SyncGPUTime"),
])

D3DSCANLINEORDERING = Enum("D3DSCANLINEORDERING", [
    "D3DSCANLINEORDERING_UNKNOWN",
    "D3DSCANLINEORDERING_PROGRESSIVE",
    "D3DSCANLINEORDERING_INTERLACED",
])

D3DDISPLAYMODEEX = Struct("D3DDISPLAYMODEEX", [
    (UINT, "Size"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "RefreshRate"),
    (D3DFORMAT, "Format"),
    (D3DSCANLINEORDERING, "ScanLineOrdering"),
])

D3DDISPLAYMODEFILTER = Struct("D3DDISPLAYMODEFILTER", [
    (UINT, "Size"),
    (D3DFORMAT, "Format"),
    (D3DSCANLINEORDERING, "ScanLineOrdering"),
])

D3DDISPLAYROTATION = Enum("D3DDISPLAYROTATION", [
    "D3DDISPLAYROTATION_IDENTITY",
    "D3DDISPLAYROTATION_90",
    "D3DDISPLAYROTATION_180",
    "D3DDISPLAYROTATION_270",
])

D3D9_RESOURCE_PRIORITY = FakeEnum(DWORD, [
    "D3D9_RESOURCE_PRIORITY_MINIMUM",
    "D3D9_RESOURCE_PRIORITY_LOW",
    "D3D9_RESOURCE_PRIORITY_NORMAL",
    "D3D9_RESOURCE_PRIORITY_HIGH",
    "D3D9_RESOURCE_PRIORITY_MAXIMUM",
])

