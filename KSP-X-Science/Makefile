assemblies := System,System.Core,UnityEngine,UnityEngine.UI,Assembly-Csharp,UnityEngine.CoreModule,UnityEngine.IMGUIModule,UnityEngine.TextRenderingModule,UnityEngine.AudioModule,UnityEngine.AnimationModule,UnityEngine.InputLegacyModule,UnityEngine.PhysicsModule,UnityEngine.ImageConversionModule
module_name := [x]\ Science!
icons := $(wildcard icons/*)
comma := ,

# the complex join creates a list of -res:icons/icon.png,ScienceChecklist.icons.icon.png words
distro/$(module_name).dll: *.cs Lib/*.cs distro $(icons)
	@echo ==== running $@ target
	mcs -t:library -r:$(assemblies) \
		$(join $(addprefix -res:,$(icons)),$(addprefix $(comma)ScienceChecklist.,$(subst /,.,$(icons)))) \
		-recurse:*.cs -out:distro/$(module_name).dll \
		-lib:$(HOME)/'Library/Application Support/Steam/steamapps/common/Kerbal Space Program/KSP.app/Contents/Resources/Data/Managed'

distro: GameData/$(module_name)
	@echo ==== running $@ target
	mkdir distro
	cp -vr GameData/$(module_name)/ distro

.PHONY: clean rebuild
clean:
	@echo ==== running $@ target
	rm -vrf distro

rebuild: clean distro/$(module_name).dll

