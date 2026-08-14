# shadow Docs - 轻量页面目录（TOC）插件
# 不依赖 jekyll-toc：读取页面原始 markdown 正文（page['content']），
# 用站点同款 kramdown 配置转换为 HTML，再用 Nokogiri 抽取 h2/h3 生成锚点目录。
# 转 HTML 可保证生成的 id 与页面真实渲染锚点完全一致。
require 'nokogiri'
require 'kramdown'

module Jekyll
  class PageTocTag < Liquid::Tag
    def render(context)
      page = context.registers[:page]
      md = page.is_a?(Hash) ? page['content'] : nil
      md = page['content'] if md.nil? && page.respond_to?(:[])
      return '' if md.nil? || md.to_s.strip.empty?

      # 取站点 kramdown 配置，但去掉语法高亮（TOC 只需标题 id，且避免 rouge 开销/异常）
      site = context.registers[:site]
      kd = (site.config['kramdown'] || {}).dup
      kd.delete('syntax_highlighter')
      kd.delete('syntax_highlighter_opts')
      kd = kd.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      html = Kramdown::Document.new(md.to_s, kd).to_html
      doc = Nokogiri::HTML.fragment(html)
      heads = doc.css('h2, h3').select { |h| (h['id'] || '').to_s.strip != '' }
      return '' if heads.empty?

      out = +'<ul class="section-nav">'
      heads.each do |h|
        id = h['id'].to_s.strip
        text = h.text.to_s.strip
        out << %(<li class="toc-entry toc-#{h.name}"><a href="##{id}">#{text}</a></li>)
      end
      out << '</ul>'
      out
    end
  end
end

Liquid::Template.register_tag('page_toc', Jekyll::PageTocTag)
