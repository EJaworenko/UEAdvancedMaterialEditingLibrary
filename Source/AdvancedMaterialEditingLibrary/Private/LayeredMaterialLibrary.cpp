#include "LayeredMaterialLibrary.h"
#include "MaterialEditor/MaterialEditorInstanceConstant.h"

void RefreshEditorMaterialInstance(UMaterialInstanceConstant* Instance)
{
	// This is necessary as the editor caches the materialLayerParameters.
	// > The material instance editor window puts MaterialLayersParameters into our StaticParameters, if we don't do this, our settings could get wiped out on first launch of the material editor.
	// > If there's ever a cleaner and more isolated way of populating MaterialLayersParameters, we should do that instead.
	UMaterialEditorInstanceConstant* MaterialEditorInstance = NewObject<UMaterialEditorInstanceConstant>(GetTransientPackage(), NAME_None, RF_Transactional);
	MaterialEditorInstance->SetSourceInstance(Instance);
}


int32 ULayeredMaterialLibrary::GetLayerCount(UMaterialInstance* Instance)
{
	int32 result = 0;
	if (Instance) {
		FMaterialLayersFunctions layers;
		Instance->GetMaterialLayers(layers);

		return layers.Layers.Num();
	}
	return result;
}

bool ULayeredMaterialLibrary::AddMaterialLayer(UMaterialInstance* Instance)
{
	FMaterialLayersFunctions layers;
	if (Instance->GetMaterialLayers(layers))
	{
		layers.AppendBlendedLayer();
		Instance->SetMaterialLayers(layers);

		return true;
	}

	return false;
}

bool ULayeredMaterialLibrary::IsLayeredMaterial(UMaterialInstance* Instance)
{
	FMaterialLayersFunctions layers;
	return Instance->GetMaterialLayers(layers);
}

/*
 The next two functions are pretty much copying what the editor does internally when changing material layers/blends
 See FMaterialPropertyHelpers::OnMaterialLayerAssetChanged
*/

bool ULayeredMaterialLibrary::AssignLayerMaterial(UMaterialInstance* Instance, int32 LayerIndex, UMaterialFunctionInterface* NewLayerFunction)
{
	FMaterialLayersFunctions layers;
	if (Instance->GetMaterialLayers(layers)) {
		layers.Layers[LayerIndex] = NewLayerFunction;
		layers.UnlinkLayerFromParent(LayerIndex);

		Instance->SetMaterialLayers(layers);

		return true;
	}

	return false;
}

bool ULayeredMaterialLibrary::AssignBlendLayer(UMaterialInstance* Instance, int32 LayerIndex, UMaterialFunctionInterface* NewBlendLayerFunction)
{
	FMaterialLayersFunctions layers;
	if (Instance->GetMaterialLayers(layers)) {
		int32 adjustedIndex = LayerIndex - 1; // To match the editor UI, but blend indices are offset by 1

		layers.Blends[adjustedIndex] = NewBlendLayerFunction;
		layers.UnlinkLayerFromParent(adjustedIndex + 1); // Blend indices are offset by 1, no blend for base layer

		Instance->SetMaterialLayers(layers);

		return true;
	}

	return false;
}

/*
 The following functions are for Layer Parameters.
*/

float ULayeredMaterialLibrary::GetLayeredMaterialScalarParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
	float Result = 0.f;
	if (Instance)
	{
		Instance->GetScalarParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Result);
	}
	return Result;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialScalarParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, float Value)
{
	if (Instance)
	{
		Instance->SetScalarParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Value);
		RefreshEditorMaterialInstance(Instance);
		return true;
	}
	return false;
}

FLinearColor ULayeredMaterialLibrary::GetLayeredMaterialVectorParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    FLinearColor Result = FLinearColor(0, 0, 0, 0);
    if (Instance)
    {
        Instance->GetVectorParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Result);
    }
    return Result;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialVectorParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FLinearColor Value)
{
    if (Instance)
    {
        Instance->SetVectorParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Value);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}

bool ULayeredMaterialLibrary::GetLayeredMaterialStaticSwitchParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
	bool bResult = false;
	if (Instance)
	{
		FGuid OutGuid;
		Instance->GetStaticSwitchParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), bResult, OutGuid);
	}
	return bResult;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialStaticSwitchParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, bool Value)
{
	if (Instance)
	{
		Instance->SetStaticSwitchParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Value);
		RefreshEditorMaterialInstance(Instance);
		return true;
	}
	return false;
}

UTexture* ULayeredMaterialLibrary::GetLayeredMaterialTextureParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
	UTexture* Result = nullptr;
	if (Instance)
	{
		Instance->GetTextureParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Result);
	}
	return Result;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialTextureParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, UTexture* Value)
{
	if (Instance)
	{
		Instance->SetTextureParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Value);
		RefreshEditorMaterialInstance(Instance);

		return true;
	}
	return false;
}

FVector4 ULayeredMaterialLibrary::GetLayeredMaterialChannelMaskParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    FLinearColor Result = FLinearColor(0, 0, 0, 0);
    if (Instance)
    {
        Instance->GetVectorParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Result);
    }
    return FVector4(Result.R, Result.G, Result.B, Result.A);
}

bool ULayeredMaterialLibrary::SetLayeredMaterialChannelMaskParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FVector4 Value)
{
    if (Instance)
    {
        FLinearColor Color(Value.X, Value.Y, Value.Z, Value.W);
        Instance->SetVectorParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::LayerParameter, LayerIndex), Color);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}

/*
 The following functions are for Blend Parameters.
*/

float ULayeredMaterialLibrary::GetLayeredMaterialBlendScalarParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    float Result = 0.f;
    if (Instance)
    {
		int32 adjustedIndex = LayerIndex - 1; // Same offset as AssignBlendLayer
        Instance->GetScalarParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Result);
    }
    return Result;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialBlendScalarParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, float Value)
{
    if (Instance)
    {
		int32 adjustedIndex = LayerIndex - 1; // Same offset as AssignBlendLayer
        Instance->SetScalarParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Value);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}

FLinearColor ULayeredMaterialLibrary::GetLayeredMaterialBlendVectorParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    FLinearColor Result = FLinearColor(0, 0, 0, 0);
    if (Instance)
    {
        int32 adjustedIndex = LayerIndex - 1;  // Same offset as AssignBlendLayer
        Instance->GetVectorParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Result);
    }
    return Result;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialBlendVectorParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FLinearColor Value)
{
    if (Instance)
    {
        int32 adjustedIndex = LayerIndex - 1;  // Same offset as AssignBlendLayer
        Instance->SetVectorParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Value);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}

bool ULayeredMaterialLibrary::GetLayeredMaterialBlendStaticSwitchParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    bool bResult = false;
    if (Instance)
    {
        FGuid OutGuid;
		int32 adjustedIndex = LayerIndex - 1; // Same offset as AssignBlendLayer
        Instance->GetStaticSwitchParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), bResult, OutGuid);
    }
    return bResult;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialBlendStaticSwitchParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, bool Value)
{
    if (Instance)
    {
		int32 adjustedIndex = LayerIndex - 1; // Same offset as AssignBlendLayer
        Instance->SetStaticSwitchParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Value);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}

UTexture* ULayeredMaterialLibrary::GetLayeredMaterialBlendTextureParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    UTexture* Result = nullptr;
    if (Instance)
    {
		int32 adjustedIndex = LayerIndex - 1; // Same offset as AssignBlendLayer
        Instance->GetTextureParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Result);
    }
    return Result;
}

bool ULayeredMaterialLibrary::SetLayeredMaterialBlendTextureParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, UTexture* Value)
{
    if (Instance)
    {
		int32 adjustedIndex = LayerIndex - 1; // Same offset as AssignBlendLayer
        Instance->SetTextureParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Value);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}

FVector4 ULayeredMaterialLibrary::GetLayeredMaterialBlendChannelMaskParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex)
{
    FLinearColor Result = FLinearColor(0, 0, 0, 0);
    if (Instance)
    {
        int32 adjustedIndex = LayerIndex - 1;
        Instance->GetVectorParameterValue(FHashedMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Result);
    }
    return FVector4(Result.R, Result.G, Result.B, Result.A);
}

bool ULayeredMaterialLibrary::SetLayeredMaterialBlendChannelMaskParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FVector4 Value)
{
    if (Instance)
    {
        int32 adjustedIndex = LayerIndex - 1;
        FLinearColor Color(Value.X, Value.Y, Value.Z, Value.W);
        Instance->SetVectorParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, EMaterialParameterAssociation::BlendParameter, adjustedIndex), Color);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}
/*
 The following functions are for Unlayered Parameters, but they don't exist by default.
*/

FVector4 ULayeredMaterialLibrary::GetMaterialInstanceChannelMaskParameterValue(UMaterialInstance* Instance, FName ParameterName, EMaterialParameterAssociation Association)
{
    FLinearColor Result = FLinearColor(0, 0, 0, 0);
    if (Instance)
    {
        Instance->GetVectorParameterValue(FHashedMaterialParameterInfo(ParameterName, Association), Result);
    }
    return FVector4(Result.R, Result.G, Result.B, Result.A);
}

bool ULayeredMaterialLibrary::SetMaterialInstanceChannelMaskParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, FVector4 Value, EMaterialParameterAssociation Association)
{
    if (Instance)
    {
        FLinearColor Color(Value.X, Value.Y, Value.Z, Value.W);
        Instance->SetVectorParameterValueEditorOnly(FMaterialParameterInfo(ParameterName, Association), Color);
        RefreshEditorMaterialInstance(Instance);
        return true;
    }
    return false;
}
