{
    'targets': [
        {
            'target_name': 'pdfwriter',
            'type': 'static_library',
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'defines': [
                'USE_BUNDLED=TRUE'
            ],
            'conditions': [
                ['OS=="mac"', {
                   'xcode_settings': {
                       'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                   }
                }]
            ],
           'msvs_settings':
			{
				'VCCLCompilerTool':
				{
					'AdditionalOptions':
						[
						'/std:c++20',
						]
				}
			},
            'dependencies': [
               '<(module_root_dir)/src/deps/LibAesgm/binding.gyp:libaesgm',
               '<(module_root_dir)/src/deps/FreeType/binding.gyp:freetype',
               '<(module_root_dir)/src/deps/LibJpeg/binding.gyp:libjpeg',
               '<(module_root_dir)/src/deps/Zlib/binding.gyp:zlib',
               '<(module_root_dir)/src/deps/LibTiff/binding.gyp:libtiff',
               '<(module_root_dir)/src/deps/LibPng/binding.gyp:libpng'
            ],
            'include_dirs': [
                '<(module_root_dir)/src/deps/LibAesgm',
                '<(module_root_dir)/src/deps/FreeType/include',
                '<(module_root_dir)/src/deps/LibTiff',
                '<(module_root_dir)/src/deps/Zlib',
                '<(module_root_dir)/src/deps/LibJpeg',
                '<(module_root_dir)/src/deps/LibPng'
            ],
           'sources':[
                'AbstractContentContext.cpp',
                'AbstractContentContext.h',
                'AbstractWrittenFont.cpp',
                'AbstractWrittenFont.h',
                'AdapterIByteReaderWithPositionToIReadPositionProvider.h',
                'ANSIFontWriter.cpp',
                'ANSIFontWriter.h',
                'ArrayOfInputStreamsStream.cpp',
                'ArrayOfInputStreamsStream.h',
                'Ascii7Encoding.cpp',
                'Ascii7Encoding.h',
                'BetweenIncluding.h',
                'CatalogInformation.cpp',
                'CatalogInformation.h',
                'CFFANSIFontWriter.cpp',
                'CFFANSIFontWriter.h',
                'CFFDescendentFontWriter.cpp',
                'CFFDescendentFontWriter.h',
                'CFFEmbeddedFontWriter.cpp',
                'CFFEmbeddedFontWriter.h',
                'CFFFileInput.cpp',
                'CFFFileInput.h',
                'CFFPrimitiveReader.cpp',
                'CFFPrimitiveReader.h',
                'CFFPrimitiveWriter.cpp',
                'CFFPrimitiveWriter.h',
                'CharStringDefinitions.h',
                'CharStringType1Interpreter.cpp',
                'CharStringType1Interpreter.h',
                'CharStringType1Tracer.cpp',
                'CharStringType1Tracer.h',
                'CharStringType2Flattener.cpp',
                'CharStringType2Flattener.h',
                'CharStringType2Interpreter.cpp',
                'CharStringType2Interpreter.h',
                'CharStringType2Tracer.cpp',
                'CharStringType2Tracer.h',
                'CIDFontWriter.cpp',
                'CIDFontWriter.h',
                'CMYKRGBColor.cpp',
                'CMYKRGBColor.h',
                'ContainerIterator.h',
                'DecryptionHelper.cpp',
                'DecryptionHelper.h',
                'Deletable.h',
                'DescendentFontWriter.cpp',
                'DescendentFontWriter.h',
                'DictionaryContext.cpp',
                'DictionaryContext.h',
                'DictOperand.h',
                'DocumentContext.cpp',
                'DocumentContext.h',
                'DocumentContextExtenderAdapter.h',
                'EFontStretch.h',
                'EHummusImageType.h',
                'EncryptionHelper.cpp',
                'EncryptionHelper.h',
                'EncryptionOptions.cpp',
                'EncryptionOptions.h',
                'EPDFVersion.h',
                'EStatusCode.h',
                'ETokenSeparator.h',
                'ExtGStateRegistry.cpp',
                'ExtGStateRegistry.h',
                'FontDescriptorWriter.cpp',
                'FontDescriptorWriter.h',
                'FreeTypeFaceWrapper.cpp',
                'FreeTypeFaceWrapper.h',
                'FreeTypeOpenTypeWrapper.cpp',
                'FreeTypeOpenTypeWrapper.h',
                'FreeTypeType1Wrapper.cpp',
                'FreeTypeType1Wrapper.h',
                'FreeTypeWrapper.cpp',
                'FreeTypeWrapper.h',
                'FSType.h',
                'GlyphUnicodeMapping.h',
                'GraphicState.cpp',
                'GraphicState.h',
                'GraphicStateStack.cpp',
                'GraphicStateStack.h',
                'IANSIFontWriterHelper.h',
                'IByteReader.h',
                'IByteReaderWithPosition.h',
                'IByteWriter.h',
                'IByteWriterWithPosition.h',
                'IContentContextListener.h',
                'IDeletable.h',
                'IDescendentFontWriter.h',
                'IDocumentContextExtender.h',
                'IFontDescriptorHelper.h',
                'IFormEndWritingTask.h',
                'IFreeTypeFaceExtender.h',
                'IndirectObjectsReferenceRegistry.cpp',
                'IndirectObjectsReferenceRegistry.h',
                'InfoDictionary.cpp',
                'InfoDictionary.h',
                'InputAESDecodeStream.cpp',
                'InputAESDecodeStream.h',
                'InputAscii85DecodeStream.cpp',
                'InputAscii85DecodeStream.h',
                'InputAsciiHexDecodeStream.cpp',
                'InputAsciiHexDecodeStream.h',
                'InputBufferedStream.cpp',
                'InputBufferedStream.h',
                'InputByteArrayStream.cpp',
                'InputByteArrayStream.h',
                'InputCharStringDecodeStream.cpp',
                'InputCharStringDecodeStream.h',
                'InputDCTDecodeStream.cpp',
                'InputDCTDecodeStream.h',
                'InputFile.cpp',
                'InputFile.h',
                'InputFileStream.cpp',
                'InputFileStream.h',
                'InputFlateDecodeStream.cpp',
                'InputFlateDecodeStream.h',
                'InputLimitedStream.cpp',
                'InputLimitedStream.h',
                'InputLZWDecodeStream.cpp',
                'InputLZWDecodeStream.h',
                'InputOffsetStream.cpp',
                'InputOffsetStream.h',
                'InputPFBDecodeStream.cpp',
                'InputPFBDecodeStream.h',
                'InputPredictorPNGOptimumStream.cpp',
                'InputPredictorPNGOptimumStream.h',
                'InputPredictorTIFFSubStream.cpp',
                'InputPredictorTIFFSubStream.h',
                'InputRC4XcodeStream.cpp',
                'InputRC4XcodeStream.h',
                'InputStreamSkipperStream.cpp',
                'InputStreamSkipperStream.h',
                'InputStringBufferStream.cpp',
                'InputStringBufferStream.h',
                'InputStringStream.cpp',
                'InputStringStream.h',
                'IOBasicTypes.h',
                'IObjectEndWritingTask.h',
                'IObjectsContextExtender.h',
                'IPageEndWritingTask.h',
                'IPDFParserExtender.h',
                'IReadPositionProvider.h',
                'IResourceWritingTask.h',
                'ITiledPatternEndWritingTask.h',
                'IType1InterpreterImplementation.h',
                'IType2InterpreterImplementation.h',
                'IWrittenFont.h',
                'JPEGImageHandler.cpp',
                'JPEGImageHandler.h',
                'JPEGImageInformation.cpp',
                'JPEGImageInformation.h',
                'JPEGImageParser.cpp',
                'JPEGImageParser.h',
                'LayeredGlyphsDrawingContext.cpp',
                'LayeredGlyphsDrawingContext.h',
                'LinearGradientShadingPatternWritingTask.cpp',
                'LinearGradientShadingPatternWritingTask.h',
                'Log.cpp',
                'Log.h',
                'MapIterator.h',
                'MD5Generator.cpp',
                'MD5Generator.h',
                'MyStringBuf.h',
                'ObjectsBasicTypes.h',
                'ObjectsContext.cpp',
                'ObjectsContext.h',
                'ObjectsContextExtenderAdapter.h',
                'OpenTypeFileInput.cpp',
                'OpenTypeFileInput.h',
                'OpenTypePrimitiveReader.cpp',
                'OpenTypePrimitiveReader.h',
                'OutputAESEncodeStream.cpp',
                'OutputAESEncodeStream.h',
                'OutputBufferedStream.cpp',
                'OutputBufferedStream.h',
                'OutputFile.cpp',
                'OutputFile.h',
                'OutputFileStream.cpp',
                'OutputFileStream.h',
                'OutputFlateDecodeStream.cpp',
                'OutputFlateDecodeStream.h',
                'OutputFlateEncodeStream.cpp',
                'OutputFlateEncodeStream.h',
                'OutputRC4XcodeStream.cpp',
                'OutputRC4XcodeStream.h',
                'OutputStreamTraits.cpp',
                'OutputStreamTraits.h',
                'OutputStringBufferStream.cpp',
                'OutputStringBufferStream.h',
                'PageContentContext.cpp',
                'PageContentContext.h',
                'PageTree.cpp',
                'PageTree.h',
                'PaintedGlyphsDrawingContext.cpp',
                'PaintedGlyphsDrawingContext.h',
                'ParsedPrimitiveHelper.cpp',
                'ParsedPrimitiveHelper.h',
                'PDFArray.cpp',
                'PDFArray.h',
                'PDFArrayIterator.cpp',
                'PDFArrayIterator.h',
                'PDFBoolean.cpp',
                'PDFBoolean.h',
                'PDFCosArray.cpp',
                'PDFCosArray.h',
                'PDFCosDict.cpp',
                'PDFCosDict.h',
                'PDFDate.cpp',
                'PDFDate.h',
                'PDFDictionary.cpp',
                'PDFDictionary.h',
                'PDFDictionaryIterator.cpp',
                'PDFDictionaryIterator.h',
                'PDFDocEncoding.cpp',
                'PDFDocEncoding.h',
                'PDFDocumentCopyingContext.cpp',
                'PDFDocumentCopyingContext.h',
                'PDFDocumentHandler.cpp',
                'PDFDocumentHandler.h',
                'PDFEmbedParameterTypes.h',
                'PDFFormXObject.cpp',
                'PDFFormXObject.h',
                'PDFHexString.cpp',
                'PDFHexString.h',
                'PDFImageXObject.cpp',
                'PDFImageXObject.h',
                'PDFIndirectObjectReference.cpp',
                'PDFIndirectObjectReference.h',
                'PDFInteger.cpp',
                'PDFInteger.h',
                'PDFLiteralString.cpp',
                'PDFLiteralString.h',
                'PDFMatrix.cpp',
                'PDFMatrix.h',
                'PDFModifiedPage.cpp',
                'PDFModifiedPage.h',
                'PDFName.cpp',
                'PDFName.h',
                'PDFNull.cpp',
                'PDFNull.h',
                'PDFObject.cpp',
                'PDFObject.h',
                'PDFObjectCast.h',
                'PDFObjectParser.cpp',
                'PDFObjectParser.h',
                'PDFPage.cpp',
                'PDFPage.h',
                'PDFPageInput.cpp',
                'PDFPageInput.h',
                'PDFPageMergingHelper.cpp',
                'PDFPageMergingHelper.h',
                'PDFParser.cpp',
                'PDFParser.h',
                'PDFParserTokenizer.cpp',
                'PDFParserTokenizer.h',
                'PDFParsingOptions.cpp',
                'PDFParsingOptions.h',
                'PDFParsingPath.cpp',
                'PDFParsingPath.h',
                'PDFReal.cpp',
                'PDFReal.h',
                'PDFRectangle.cpp',
                'PDFRectangle.h',
                'PDFStream.cpp',
                'PDFStream.h',
                'PDFStreamInput.cpp',
                'PDFStreamInput.h',
                'PDFSymbol.cpp',
                'PDFSymbol.h',
                'PDFTextString.cpp',
                'PDFTextString.h',
                'PDFTiledPattern.cpp',
                'PDFTiledPattern.h',
                'PDFUsedFont.cpp',
                'PDFUsedFont.h',
                'PDFWriter.cpp',
                'PDFWriter.h',
                'PFMFileReader.cpp',
                'PFMFileReader.h',
                'PNGImageHandler.cpp',
                'PNGImageHandler.h',
                'PrimitiveObjectsWriter.cpp',
                'PrimitiveObjectsWriter.h',
                'ProcsetResourcesConstants.h',
                'PSBool.cpp',
                'PSBool.h',
                'RC4.cpp',
                'RC4.h',
                'RefCountObject.cpp',
                'RefCountObject.h',
                'RefCountPtr.h',
                'ResourcesDictionary.cpp',
                'ResourcesDictionary.h',
                'SafeBufferMacrosDefs.h',
                'ShadingWriter.cpp',
                'ShadingWriter.h',
                'SimpleGlyphsDrawingContext.cpp',
                'SimpleGlyphsDrawingContext.h',
                'SimpleStringTokenizer.cpp',
                'SimpleStringTokenizer.h',
                'Singleton.h',
                'SingleValueContainerIterator.h',
                'StandardEncoding.cpp',
                'StandardEncoding.h',
                'StateReader.cpp',
                'StateReader.h',
                'StateWriter.cpp',
                'StateWriter.h',
                'SweepGradientShadingPatternWritingTask.cpp',
                'SweepGradientShadingPatternWritingTask.h',
                'TIFFImageHandler.cpp',
                'TIFFImageHandler.h',
                'TiffUsageParameters.cpp',
                'TiffUsageParameters.h',
                'TiledPatternContentContext.cpp',
                'TiledPatternContentContext.h',
                'Timer.cpp',
                'Timer.h',
                'TimersRegistry.cpp',
                'TimersRegistry.h',
                'Trace.cpp',
                'Trace.h',
                'TrailerInformation.cpp',
                'TrailerInformation.h',
                'TrueTypeANSIFontWriter.cpp',
                'TrueTypeANSIFontWriter.h',
                'TrueTypeDescendentFontWriter.cpp',
                'TrueTypeDescendentFontWriter.h',
                'TrueTypeEmbeddedFontWriter.cpp',
                'TrueTypeEmbeddedFontWriter.h',
                'TrueTypePrimitiveWriter.cpp',
                'TrueTypePrimitiveWriter.h',
                'Type1Input.cpp',
                'Type1Input.h',
                'Type1ToCFFEmbeddedFontWriter.cpp',
                'Type1ToCFFEmbeddedFontWriter.h',
                'Type1ToType2Converter.cpp',
                'Type1ToType2Converter.h',
                'Type2CharStringWriter.cpp',
                'Type2CharStringWriter.h',
                'UnicodeString.cpp',
                'UnicodeString.h',
                'UppercaseSequance.cpp',
                'UppercaseSequance.h',
                'UsedFontsRepository.cpp',
                'UsedFontsRepository.h',
                'WinAnsiEncoding.cpp',
                'WinAnsiEncoding.h',
                'WrittenFontCFF.cpp',
                'WrittenFontCFF.h',
                'WrittenFontRepresentation.h',
                'WrittenFontTrueType.cpp',
                'WrittenFontTrueType.h',
                'XCryptionCommon.cpp',
                'XCryptionCommon.h',
                'XObjectContentContext.cpp',
                'XObjectContentContext.h',
                'RadialGradientShadingPatternWritingTask.cpp',
                'RadialGradientShadingPatternWritingTask.h'
            ]
        }
    ]        
}
