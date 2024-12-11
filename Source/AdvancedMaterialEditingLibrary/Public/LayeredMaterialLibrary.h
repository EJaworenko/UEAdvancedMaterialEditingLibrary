#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "Materials/MaterialInstanceConstant.h"
#include "LayeredMaterialLibrary.generated.h"

/**
 *
 */
UCLASS()
class ADVANCEDMATERIALEDITINGLIBRARY_API ULayeredMaterialLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static int32 GetLayerCount(UMaterialInstance* Instance);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool AddMaterialLayer(UMaterialInstance* Instance);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool IsLayeredMaterial(UMaterialInstance* Instance);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool AssignLayerMaterial(UMaterialInstance* Instance, int32 LayerIndex, UMaterialFunctionInterface* NewLayerFunction);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool AssignBlendLayer(UMaterialInstance* Instance, int32 LayerIndex, UMaterialFunctionInterface* NewBlendLayerFunction);

	// Parameter value getters and setters for material layers

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static float GetLayeredMaterialScalarParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialScalarParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, float Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static FLinearColor GetLayeredMaterialVectorParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialVectorParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FLinearColor Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool GetLayeredMaterialStaticSwitchParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialStaticSwitchParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, bool Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static UTexture* GetLayeredMaterialTextureParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialTextureParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, UTexture* Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static FVector4 GetLayeredMaterialChannelMaskParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialChannelMaskParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FVector4 Value);

	// Parameter value getters and setters for blend layers

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static float GetLayeredMaterialBlendScalarParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialBlendScalarParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, float Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static FLinearColor GetLayeredMaterialBlendVectorParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialBlendVectorParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FLinearColor Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool GetLayeredMaterialBlendStaticSwitchParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialBlendStaticSwitchParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, bool Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static UTexture* GetLayeredMaterialBlendTextureParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialBlendTextureParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, UTexture* Value);

	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static FVector4 GetLayeredMaterialBlendChannelMaskParameterValue(UMaterialInstance* Instance, FName ParameterName, int32 LayerIndex);
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetLayeredMaterialBlendChannelMaskParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, int32 LayerIndex, FVector4 Value);

	// For non-layered materials
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static FVector4 GetMaterialInstanceChannelMaskParameterValue(UMaterialInstance* Instance, FName ParameterName, EMaterialParameterAssociation Association = EMaterialParameterAssociation::GlobalParameter);
	// For non-layered materials
	UFUNCTION(BlueprintCallable, Category = "AdvancedMaterialEditingLibrary")
		static bool SetMaterialInstanceChannelMaskParameterValue(UMaterialInstanceConstant* Instance, FName ParameterName, FVector4 Value, EMaterialParameterAssociation Association = EMaterialParameterAssociation::GlobalParameter);
};
